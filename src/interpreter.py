
from antlr4 import *
from AingalLangLexer import AingalLangLexer
from AingalLangParser import AingalLangParser
from AingalLangParserVisitor import AingalLangParserVisitor
import math


class BreakStatement:
    pass

class FunctionReturn(Exception):
    def __init__(self, value):
        self.value = value

class InterpreterError(Exception):
    def __init__(self, message, line=None, column=None, code_line=None, suggestion=None):
        self.message = message
        self.line = line
        self.column = column
        self.code_line = code_line
        self.suggestion = suggestion
        
    def __str__(self):
        parts = [f"❌ Runtime Error: {self.message}"]
        if self.line is not None:
            parts.append(f"❌ At line {self.line}")
        if self.code_line is not None:
            parts.append(f"❌ Code: {self.code_line}")
            if self.column is not None:
                pointer = " " * self.column + "^"
                parts.append(f"❌        {pointer}")
        if self.suggestion is not None:
            parts.append(f"❌ Suggestion: {self.suggestion}")
        return "\n".join(parts)

class Scope:
    def __init__(self, parent=None):
        self.variables = {}
        self.parameters = set()  # Track parameters separately
        self.parent = parent

    def set_variable(self, name, value, is_param=False):
        if is_param:
            self.parameters.add(name)
        self.variables[name] = value

    def has_variable(self, name):
        return name in self.variables

    def is_parameter(self, name):
        if name in self.parameters:
            return True
        if self.parent:
            return self.parent.is_parameter(name)
        return False

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get_variable(name)
        else:
            raise Exception(f"Variable '{name}' not found in any scope")

class Interpreter(AingalLangParserVisitor):
    def __init__(self, debug=False):
        super().__init__()
        self.global_scope = Scope()
        self.current_scope = self.global_scope
        self.memory = {}
        self.variables = {}
        self.functions = {}        
        self.output_lines = []
        self.call_stack = []
        self.debug = debug

    def push_env(self):
        self.current_scope = Scope(parent=self.current_scope)

    def pop_env(self):
        if self.current_scope.parent:
            self.current_scope = self.current_scope.parent
        else:
            raise Exception("Cannot pop global scope")

    def set_var(self, name, value):
        scope = self.global_scope
        while scope:
            if scope.has_variable(name):  # ✅ use has_variable here
                scope.set_variable(name, value)
                return
            scope = scope.parent
        # If not found, define in current scope
        self.global_scope.set_variable(name, value)

    def get_var(self, name):
        return self.current_scope.get_variable(name)

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if result is not None and not isinstance(result, BreakStatement):
                self.output_lines.append(str(result))
        return self.output_lines
    
    def visitVariableDeclaration(self, ctx):
        if ctx.scopedIdentifier():
            # Don't visit scopedIdentifier (returns value), instead parse text
            scoped_name = ctx.scopedIdentifier().getText()  # e.g. "parent::x"
            value = self.visit(ctx.expression())
            type_ctx = ctx.typeAnnotation()
            declared_type = type_ctx.getText().lower() if type_ctx else None
            if declared_type:
                value = self.cast_value(value, declared_type)

            scope, var_name = self.resolve_scope_for_assignment(scoped_name)
            if scope.has_variable(var_name):
                raise Exception(f"Variable '{var_name}' already declared in this scope.")
            scope.set_variable(var_name, value)
        else:
            name = ctx.leftHandSide().getText()
            value = self.visit(ctx.expression())
            type_ctx = ctx.typeAnnotation()
            declared_type = type_ctx.getText().lower() if type_ctx else None
            
            if self.current_scope.is_parameter(name):
                line = ctx.start.line
                column = ctx.start.column
                code_line = self.get_source_line(ctx)
                raise InterpreterError(
                    message=f"Cannot redeclare parameter '{name}' in this scope",
                    line=line,
                    column=column,
                    code_line=code_line,
                    suggestion="Parameters cannot be redeclared in the same function scope"
                )
            
            # Check if variable already exists in current scope
            if self.current_scope.has_variable(name):
                raise Exception(f"Variable '{name}' is already declared in this scope")
                
            if declared_type:
                value = self.cast_value(value, declared_type)
            self.current_scope.set_variable(name, value)
        return None
    
    def lookup_variable(self, name):
        return self.current_scope.get_variable(name)

    def visitFunctionDeclaration(self, ctx):
        name = ctx.IDENTIFIER().getText()
        param_list = []

        if ctx.parameter():
            for typed_param in ctx.parameter().typedParameter():
                param_name = typed_param.IDENTIFIER().getText()
                param_list.append(param_name)

        body = ctx.blockStatement()
        self.functions[name] = {
            "params": param_list,
            "body": body,
            "scope": self.current_scope
        }
        return None

    def visitFunctionCall(self, ctx):
        #print("New visitFunctionCall reached")

        func_name = ctx.IDENTIFIER().getText()
        args = []

        if ctx.argumentList():
            for expr in ctx.argumentList().expression():
                arg_val = self.visit(expr)
                args.append(arg_val)

        #print(f"Calling function: {func_name} with args: {args}")
        result = self.callFunction(func_name, args)
        return result        

    def callFunction(self, name, args):
        func = self.functions[name]
        param_names = func["params"]
        body = func["body"]
        defining_scope = func["scope"]

        if len(param_names) != len(args):
            raise Exception(f"Function '{name}' expects {len(param_names)} args, got {len(args)}")

        # Create new scope with defining_scope as parent
        local_scope = Scope(parent=defining_scope)

        # Set parameter values and mark them as parameters
        for pname, arg in zip(param_names, args):
            local_scope.set_variable(pname, arg, is_param=True)

        previous_scope = self.current_scope
        self.current_scope = local_scope

        try:
            result = self.visit(body)
        except FunctionReturn as fr:
            result = fr.value
        finally:
            self.current_scope = previous_scope

        print(f"Function {name} returned: {return_value}")
        return return_value
    
    def visitBuiltInFunctions(self, ctx):
        if ctx.POWER_FUNC():
            base = self.visit(ctx.numExpression(0))
            exponent = self.visit(ctx.numExpression(1))
            return math.pow(base, exponent)

        elif ctx.SIN_FUNC():
            value = self.visit(ctx.numExpression(0))
            return math.sin(value)

        elif ctx.COS_FUNC():
            value = self.visit(ctx.numExpression(0))
            return math.cos(value)

        elif ctx.TAN_FUNC():
            value = self.visit(ctx.numExpression(0))
            return math.tan(value)

        elif ctx.CTAN_FUNC():
            value = self.visit(ctx.numExpression(0))
            tan_val = math.tan(value)
            if tan_val == 0:
                raise ZeroDivisionError("Cotangent undefined: tan(value) = 0")
            return 1 / tan_val

        else:
            raise Exception("Unknown built-in function")


    def visitIdentifier(self, ctx):
        var_name = ctx.getText()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise Exception(f"Undefined variable: {var_name}")
        
    def visitScopedIdentifier(self, ctx):
        levels = len(ctx.getTokens(AingalLangParser.PARENT_SCOPE))
        name = ctx.IDENTIFIER().getText()

        current_scope = self.current_scope.parent if self.current_scope.parent else self.current_scope
        
        for _ in range(levels):
            if current_scope.parent is None:
                line = ctx.start.line
                column = ctx.start.column
                code_line = self.get_source_line(ctx)
                raise InterpreterError(
                    message=f"No parent scope exists while resolving 'parent::{name}'",
                    line=line,
                    column=column,
                    code_line=code_line,
                    suggestion="Try using fewer 'parent::' levels - you exceeded the available scope depth"
                )
            current_scope = current_scope.parent

        return current_scope.get_variable(name)

    
    def visitBlockStatement(self, ctx):
        self.push_env()
        for stmt in ctx.statement():
            self.visit(stmt)
        self.pop_env()

    
    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.expression())
        raise FunctionReturn(value)

    def visitStatement(self, ctx):
        result = self.visitChildren(ctx)

        if ctx.functionCall() and result is not None:
            #print("DEBUG: Standalone function call result:", result)
            self.output_lines.append(" ")

        return None

    def visitReassignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        if name not in self.variables:
            raise Exception(f"Variable '{name}' not defined.")
        value = self.visit(ctx.numExpression())
        if ctx.ADD_TO():
            self.variables[name] += value
        elif ctx.SUBTRACT_FROM():
            self.variables[name] -= value
        elif ctx.TIMES():
            self.variables[name] *= value
        elif ctx.DIVIDE_FROM():
            self.variables[name] /= value
        return self.variables[name]
    
    def resolve_scope_for_assignment(self, scoped_name):
        # scoped_name might be e.g. "parent::parent::x"
        parts = scoped_name.split("::")
        var_name = parts[-1]
        levels = len(parts) - 1

        scope = self.current_scope
        for _ in range(levels):
            if scope.parent is None:
                raise Exception(f"No parent scope exists while resolving assignment to '{scoped_name}'")
            scope = scope.parent

        return scope, var_name

    def visitDisplayStatement(self, ctx):
        expressions = ctx.expression()
        results = [self.visit(expr) for expr in expressions]
        display_output = ' '.join(str(r) for r in results)
        print("DEBUG: Displaying", results)
        self.output_lines.append(display_output)
        return None

    def visitNumExpression(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))

            if op == '+':
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                else:
                    return left + right
            elif op == '-':
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left - right
                else:
                    raise TypeError(f"Unsupported operand types for -: {type(left)} and {type(right)}")
        return self.visit(ctx.getChild(0))

    def visitTerm(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            if op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '%':
                return left % right
        return self.visit(ctx.getChild(0))

    def visitUnaryPlus(self, ctx):
        return +self.visit(ctx.factor())

    def visitUnaryMinus(self, ctx):
        return -self.visit(ctx.factor())

    def visitFactorNumber(self, ctx):
        return float(ctx.NUMBER().getText())

    def visitFactorIdentifier(self, ctx):
        name = ctx.IDENTIFIER().getText()
        return self.lookup_variable(name)

    def visitFactorString(self, ctx):
        return ctx.STRING().getText().strip('"')

    def visitFactorParens(self, ctx):
        return self.visit(ctx.numExpression())

    def visitFactorFunctionCall(self, ctx):
        return self.visit(ctx.functionCall())

    def visitFactorOperation(self, ctx):
        return self.visit(ctx.operation())
    
    def visitFactorscopedIdentifier(self, ctx):
        return self.visit(ctx.scopedIdentifier())

    def visitOperation(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        if var_name not in self.memory:
            raise Exception(f"Variable '{var_name}' not defined.")

        current_value = self.memory[var_name]
        if not isinstance(current_value, (int, float)):
            raise Exception(f"Cannot increment/decrement non-numeric variable '{var_name}'.")

        if ctx.INCREMENT():
            self.memory[var_name] = current_value + 1
        elif ctx.DECREMENT():
            self.memory[var_name] = current_value - 1

        return self.memory[var_name]
    
    def visitNumComparison(self, ctx):
        left = self.visit(ctx.numExpression(0))
        right = self.visit(ctx.numExpression(1))
        op = ctx.comparisonOp().getText()
        return self.evaluateBinaryOp(left, right, op)

    def visitStringComparison(self, ctx):
        left = self.visit(ctx.stringExpression(0))
        right = self.visit(ctx.stringExpression(1))
        op = ctx.getChild(1).getText()
        return (left == right) if op == "==" else (left != right)

    def visitMatrixComparison(self, ctx):
        left = self.visit(ctx.matrixExpression(0))
        right = self.visit(ctx.matrixExpression(1))
        op = ctx.getChild(1).getText()
        return (left == right) if op == "==" else (left != right)

    def transpose_matrix(self, matrix):
        if not matrix or not matrix[0]:
            return []
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def invert_matrix(self, matrix):
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise Exception("Only 2x2 matrix inversion supported")

        a, b = matrix[0]
        c, d = matrix[1]
        determinant = a * d - b * c

        if determinant == 0:
            raise Exception("Matrix is not invertible")

        inverse = [
            [d / determinant, -b / determinant],
            [-c / determinant, a / determinant]
        ]
        return inverse

    def visitMatrixExpression(self, ctx):
        matrix = self.visit(ctx.matrixAtom())

        if ctx.INVERT_MATRIX():
            return self.invert_matrix(matrix)

        if ctx.TRANSPOSITION():
            return self.transpose_matrix(matrix)

        return matrix

    def visitMatrixAtom(self, ctx):
        if ctx.IDENTIFIER():
            return self.lookup_variable(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.matrixConstruction())

    def visitMatrixConstruction(self, ctx):
        rows = []
        for rowCtx in ctx.row():
            row = [self.visit(value) for value in rowCtx.value()]
            rows.append(row)
            print("DEBUG row:", row)
        return rows

    def visitValue(self, ctx):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.IDENTIFIER():
            value = self.lookup_variable(ctx.IDENTIFIER().getText())
            if isinstance(value, list) and any(isinstance(row, list) for row in value):
                raise Exception("Matrix cannot contain another matrix as an element")
            return value
        elif ctx.matrixExpression():
            raise Exception("Matrix cannot contain another matrix as an element")
        else:
            raise Exception("Invalid matrix value: must be a number or scalar variable")

    def visitCastExpression(self, ctx):
        type_str = ctx.typeAnnotation().getText().lower()
        value = self.visit(ctx.factor())
        return self.cast_value(value, type_str)

    def cast_value(self, value, type_str):
        if type_str == "int":
            return int(float(value))  # float → int works
        elif type_str == "float":
            return float(value)
        elif type_str == "bool":
            if isinstance(value, str):
                return value.lower() == "true"
            return bool(value)
        elif type_str == "string":
            return str(value)
        elif type_str == "matrix":
            # Assume matrix casting is only allowed on proper nested lists
            if isinstance(value, list) and all(isinstance(row, list) for row in value):
                return value
            raise Exception("Invalid matrix format")
        else:
            raise Exception(f"Unknown type: {type_str}")


    def visitBoolExpression(self, ctx):
        return self.visitChildren(ctx)
    
    def visitCastExpression(self, ctx):
        target_type = ctx.typeAnnotation().getText().lower()
        value = self.visit(ctx.factor())
        
        if target_type == 'int':
            if isinstance(value, bool):
                return 1 if value else 0
            try:
                return int(float(value))  # Handle cases where value is string "1" or float 1.5
            except ValueError:
                raise Exception(f"Cannot cast {value} to int")
        elif target_type == 'float':
            try:
                return float(value)
            except ValueError:
                raise Exception(f"Cannot cast {value} to float")
        elif target_type == 'bool':
            if isinstance(value, str):
                return value.lower() == 'true'
            return bool(value)
        elif target_type == 'string':
            return str(value)
        else:
            raise Exception(f"Unsupported cast type: {target_type}")

    def visitLogicOr(self, ctx):
        for i in range(len(ctx.boolAndExpression())):
            if self.visit(ctx.boolAndExpression(i)):
                return True
        return False

    def visitLogicAnd(self, ctx):
        for i in range(len(ctx.boolNotExpression())):
            if not self.visit(ctx.boolNotExpression(i)):
                return False
        return True

    def visitLogicNot(self, ctx):
        return not self.visit(ctx.boolNotExpression())

    def visitLogicPrimaryWrap(self, ctx):
        return self.visit(ctx.boolPrimary())

    def visitLogicParen(self, ctx):
        return self.visit(ctx.boolExpression())

    def visitTrueLiteral(self, ctx):
        return True

    def visitFalseLiteral(self, ctx):
        return False

    def visitLogicIdentifier(self, ctx):
        name = ctx.IDENTIFIER().getText()
        return bool(self.lookup_variable(name))

    def visitIfStatement(self, ctx):
        if self.visit(ctx.boolExpression(0)):
            stmt_or_block = ctx.statement(0) or ctx.blockStatement(0)
            if stmt_or_block:
                return self.visit(stmt_or_block)

        for i in range(len(ctx.ELSE_IF())):
            if self.visit(ctx.boolExpression(i + 1)):
                stmt_or_block = ctx.statement(i + 1) or ctx.blockStatement(i + 1)
                if stmt_or_block:
                    return self.visit(stmt_or_block)

        if ctx.ELSE():
            num_ifs = 1 + len(ctx.ELSE_IF())
            stmt_or_block = ctx.statement(num_ifs) or ctx.blockStatement(num_ifs)
            if stmt_or_block:
                return self.visit(stmt_or_block)

        return None


    def visitLoopIfStatement(self, ctx):
        if self.visit(ctx.boolExpression(0)):
            if ctx.loopStatements(0):
                return self.visit(ctx.loopStatements(0))
            elif ctx.statement(0):
                return self.visit(ctx.statement(0))

        for i in range(1, len(ctx.boolExpression())):
            if self.visit(ctx.boolExpression(i)):
                if ctx.loopStatements(i):
                    return self.visit(ctx.loopStatements(i))
                elif ctx.statement(i):
                    return self.visit(ctx.statement(i))

        if ctx.ELSE(): 
            idx = len(ctx.boolExpression())
            if len(ctx.loopStatements()) > idx:
                return self.visit(ctx.loopStatements(idx))
            elif len(ctx.statement()) > idx:
                return self.visit(ctx.statement(idx))

        return None

    def visitBreakStatement(self, ctx):
        return BreakStatement()
    
    def visitLoopStatements(self, ctx):
        if ctx.loopStatement():
            return self.visit(ctx.loopStatement())
        elif ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        elif ctx.reassignment():
            return self.visit(ctx.reassignment())
        elif ctx.functionDeclaration():
            return self.visit(ctx.functionDeclaration())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.blockStatement():
            return self.visit(ctx.blockStatement())
        elif ctx.displayStatement():
            return self.visit(ctx.displayStatement())


    def visitWhileLoop(self, ctx):
        while self.visit(ctx.boolExpression()):
            self.push_env()  

            for stmt in ctx.loopStatements():
                result = self.visit(stmt)
                if isinstance(result, BreakStatement):
                    self.pop_env()
                    return
                if result is not None:
                    self.pop_env()
                    return result

            self.pop_env()  
        return None

            
    def visitForLoop(self, ctx):
        if ctx.forInit():
            self.visit(ctx.forInit())

        while self.visit(ctx.cond): 
            self.push_env()  

            result = self.visit(ctx.forBody())
            if isinstance(result, BreakStatement):
                self.pop_env()
                return

            self.pop_env()

            self.visit(ctx.forUpdate())


    def evaluateBinaryOp(self, left, right, op):
        if op == '+': return left + right
        elif op == '-': return left - right
        elif op == '*': return left * right
        elif op == '/': return left / right
        elif op == '%': return left % right
        elif op == '<': return left < right
        elif op == '>': return left > right
        elif op == '==': return left == right
        elif op == '!=': return left != right
        elif op == '<=': return left <= right
        elif op == '>=': return left >= right
        else: raise Exception(f"Unknown operator {op}")

    def visitExpression(self, ctx):
        if ctx.numExpression():
            return self.visit(ctx.numExpression())
        elif ctx.boolExpression():
            return self.visit(ctx.boolExpression())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.builtInFunctions():
            return self.visit(ctx.builtInFunctions())
        elif ctx.matrixExpression():
            return self.visit(ctx.matrixExpression())
        elif ctx.stringExpression():
            return self.visit(ctx.stringExpression())
        elif ctx.scopedIdentifier():
            return self.visit(ctx.scopedIdentifier())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.lookup_variable(name)
        return None
