parser grammar AingalLangParser;

options { tokenVocab=AingalLangLexer; }

// Entry point
program : START_PROGRAM statement+ END_PROGRAM ;

// Statements
statement: 
<<<<<<< HEAD
    functionCall
=======
      variableDeclaration
    | reassignment
    | functionDeclaration
    | functionCall
    | returnStatement
    | displayStatement
>>>>>>> 23e3f25928a7f4a9824f1e810d909891765f1633
    | ifStatement
    | loopStatement
    | variableDeclaration
    | reassignment
    | functionDeclaration
    | functionCall
    | returnStatement
    | displayStatement
    | forLoop
    | whileLoop
    | blockStatement
    | operation
    ;

loopStatements:
      loopStatement
    | variableDeclaration
    | reassignment
    | functionDeclaration
    | returnStatement
    | ifStatement
    | blockStatement
    | BREAK
    | displayStatement
    ;


// Variable Declaration & Assignment
variableDeclaration
    : SET? (scopedIdentifier | leftHandSide) TO expression typeAnnotation?
    ;

matrixExpression: (INVERT_MATRIX)? matrixAtom (TRANSPOSITION)?;
matrixAtom: IDENTIFIER | matrixConstruction;

matrixConstruction: LBRACK row (SEMICOLON row)* RBRACK;
row: value (COMMA value)*;
value: NUMBER | IDENTIFIER;

stringExpression: (STRING | IDENTIFIER) ( PLUS (STRING | IDENTIFIER))*;


expression:
      functionCall
    | builtInFunctions
    | numExpression
    | boolExpression
    | matrixExpression
    | stringExpression
    | NUMBER
    | STRING
    | scopedIdentifier
    | IDENTIFIER
    | '(' expression ')'
    ;

scopedIdentifier
    : (PARENT_SCOPE DCOLON)+ IDENTIFIER
    ;

typeAnnotation: TYPE_STRING | TYPE_INT | TYPE_FLOAT | TYPE_BOOL | TYPE_MATRIX;


// Function Declaration
functionDeclaration
    : DEFINE_FUNCTION IDENTIFIER LPAREN parameter? RPAREN blockStatement END_FUNCTION
    ;

// Parameters and Arguments
parameter
    : typedParameter (COMMA typedParameter)*
    ;

typedParameter
    : IDENTIFIER typeAnnotation?
    ;

// Return
returnStatement
    : RETURN expression
    ;

// Function Call
functionCall
    : CALL? IDENTIFIER LPAREN argumentList? RPAREN
    ;

argumentList
    : expression (COMMA expression)*
    ;


builtInFunctions:POWER_FUNC LPAREN numExpression COMMA numExpression RPAREN
                |
             (SIN_FUNC | COS_FUNC | TAN_FUNC | CTAN_FUNC )
              LPAREN numExpression RPAREN;


ifStatement: IF LPAREN boolExpression RPAREN (statement | blockStatement)
             (ELSE_IF LPAREN boolExpression RPAREN (statement | blockStatement))*
             (ELSE (statement | blockStatement))?;
loopIfStatement: IF LPAREN boolExpression RPAREN (LBRACE loopStatements+ RBRACE | statement)

<<<<<<< HEAD
=======
             (ELSE_IF LPAREN boolExpression RPAREN (LBRACE loopStatements+ RBRACE | statement))*

             (ELSE (LBRACE loopStatements+ RBRACE | statement))?;

>>>>>>> 23e3f25928a7f4a9824f1e810d909891765f1633
loopStatement: forLoop | whileLoop;

forLoop
    : FOR LPAREN forInit? SEMICOLON
              cond=boolExpression SEMICOLON
              forUpdate RPAREN
      forBody;

forInit
    : IDENTIFIER
    | variableDeclaration
    ;

forUpdate
    : variableDeclaration
    | reassignment
    | operation
    ;

forBody
    : LBRACE loopStatements+ RBRACE
    | statement
    ;

whileLoop:
           WHILE LPAREN boolExpression RPAREN
           (LBRACE loopStatements+ RBRACE | statement);

// Display
displayStatement: DISPLAY expression (',' expression)*;

blockStatement: LBRACE statement* RBRACE ;

// Expressions
numExpression : numExpression (PLUS|MINUS) term 
    | term;

term: term (MULTIPLY|DIVIDED_BY|MODULO) factor
    | factor;

factor
    : PLUS factor                              #unaryPlus
    | MINUS factor                             #unaryMinus
    | functionCall                             #factorFunctionCall
    | NUMBER                                   #factorNumber
    | scopedIdentifier                         #factorscopedIdentifier
    | IDENTIFIER                               #factorIdentifier
    | STRING                                   #factorString
    | operation                                #factorOperation
    | LPAREN numExpression RPAREN              #factorParens
    | LPAREN typeAnnotation RPAREN factor        #castExpression
    ;

operation : IDENTIFIER (INCREMENT | DECREMENT) SEMICOLON? ;

reassignment: (scopedIdentifier | IDENTIFIER) ((ADD_TO STRING | ADD_TO numExpression)
                          | SUBTRACT_FROM numExpression
                          | DIVIDE_FROM numExpression
                          | TIMES numExpression)
               SEMICOLON;

boolExpression
    : boolOrExpression
    ;

boolOrExpression
    : boolAndExpression (OR boolAndExpression)*       #logicOr
    ;

boolAndExpression
    : boolNotExpression (AND boolNotExpression)*      #logicAnd
    ;

boolNotExpression
    : NOT boolNotExpression                           #logicNot
    | boolPrimary                                     #logicPrimaryWrap
    ;

boolPrimary
    : numExpression comparisonOp numExpression        #numComparison
    | stringExpression (EQUALS | NOT_EQUALS) stringExpression   #stringComparison
    | matrixExpression (EQUALS | NOT_EQUALS) matrixExpression   #matrixComparison
    | LPAREN boolExpression RPAREN                    #logicParen
    | TRUE_VALUE                                      #trueLiteral
    | FALSE_VALUE                                     #falseLiteral
    | IDENTIFIER                                      #logicIdentifier
    ;


// Comparison Operators
comparisonOp
    : EQUALS
    | NOT_EQUALS
    | GREATER_THAN
    | LESS_THAN
    | GREATER_EQUAL
    | LESS_EQUAL
    ;
