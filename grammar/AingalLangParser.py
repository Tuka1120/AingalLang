# Generated from AingalLangParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,70,461,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        1,0,1,0,4,0,83,8,0,11,0,12,0,84,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,102,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,113,8,2,1,3,3,3,116,8,3,1,3,1,3,3,3,120,8,3,1,3,
        1,3,1,3,3,3,125,8,3,1,4,3,4,128,8,4,1,4,1,4,3,4,132,8,4,1,5,1,5,
        3,5,136,8,5,1,6,1,6,1,6,1,6,5,6,142,8,6,10,6,12,6,145,9,6,1,6,1,
        6,1,7,1,7,1,7,5,7,152,8,7,10,7,12,7,155,9,7,1,8,1,8,1,9,1,9,1,9,
        5,9,162,8,9,10,9,12,9,165,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,181,8,10,1,11,1,11,4,11,
        185,8,11,11,11,12,11,186,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,
        3,13,197,8,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,206,8,14,10,
        14,12,14,209,9,14,1,15,1,15,3,15,213,8,15,1,16,1,16,1,16,1,17,3,
        17,219,8,17,1,17,1,17,1,17,3,17,224,8,17,1,17,1,17,1,18,1,18,1,18,
        5,18,231,8,18,10,18,12,18,234,9,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,3,19,248,8,19,1,20,1,20,1,20,1,20,
        1,20,1,20,3,20,256,8,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,264,8,
        20,5,20,266,8,20,10,20,12,20,269,9,20,1,20,1,20,1,20,3,20,274,8,
        20,3,20,276,8,20,1,21,1,21,3,21,280,8,21,1,22,1,22,1,22,3,22,285,
        8,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,3,23,296,8,23,
        1,24,1,24,1,24,3,24,301,8,24,1,25,1,25,4,25,305,8,25,11,25,12,25,
        306,1,25,1,25,1,25,3,25,312,8,25,1,26,1,26,1,26,1,26,1,26,1,26,4,
        26,320,8,26,11,26,12,26,321,1,26,1,26,1,26,3,26,327,8,26,1,27,1,
        27,1,27,1,27,5,27,333,8,27,10,27,12,27,336,9,27,1,28,1,28,5,28,340,
        8,28,10,28,12,28,343,9,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,
        5,29,353,8,29,10,29,12,29,356,9,29,1,30,1,30,1,30,1,30,1,30,1,30,
        5,30,364,8,30,10,30,12,30,367,9,30,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        3,31,388,8,31,1,32,1,32,1,32,3,32,393,8,32,1,33,1,33,3,33,397,8,
        33,1,33,1,33,1,33,1,33,3,33,403,8,33,1,33,1,33,1,33,1,33,1,33,1,
        33,3,33,411,8,33,1,33,1,33,1,34,1,34,1,35,1,35,1,35,5,35,420,8,35,
        10,35,12,35,423,9,35,1,36,1,36,1,36,5,36,428,8,36,10,36,12,36,431,
        9,36,1,37,1,37,1,37,3,37,436,8,37,1,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,
        3,38,457,8,38,1,39,1,39,1,39,0,2,58,60,40,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,0,9,2,0,53,53,68,68,2,0,54,54,68,68,1,
        0,55,59,1,0,64,67,1,0,22,23,1,0,24,26,1,0,34,35,2,0,27,27,38,38,
        2,0,27,31,38,38,510,0,80,1,0,0,0,2,101,1,0,0,0,4,112,1,0,0,0,6,115,
        1,0,0,0,8,127,1,0,0,0,10,135,1,0,0,0,12,137,1,0,0,0,14,148,1,0,0,
        0,16,156,1,0,0,0,18,158,1,0,0,0,20,180,1,0,0,0,22,184,1,0,0,0,24,
        190,1,0,0,0,26,192,1,0,0,0,28,202,1,0,0,0,30,210,1,0,0,0,32,214,
        1,0,0,0,34,218,1,0,0,0,36,227,1,0,0,0,38,247,1,0,0,0,40,249,1,0,
        0,0,42,279,1,0,0,0,44,281,1,0,0,0,46,295,1,0,0,0,48,300,1,0,0,0,
        50,311,1,0,0,0,52,313,1,0,0,0,54,328,1,0,0,0,56,337,1,0,0,0,58,346,
        1,0,0,0,60,357,1,0,0,0,62,387,1,0,0,0,64,389,1,0,0,0,66,396,1,0,
        0,0,68,414,1,0,0,0,70,416,1,0,0,0,72,424,1,0,0,0,74,435,1,0,0,0,
        76,456,1,0,0,0,78,458,1,0,0,0,80,82,5,1,0,0,81,83,3,2,1,0,82,81,
        1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,
        86,87,5,2,0,0,87,1,1,0,0,0,88,102,3,34,17,0,89,102,3,40,20,0,90,
        102,3,42,21,0,91,102,3,6,3,0,92,102,3,66,33,0,93,102,3,26,13,0,94,
        102,3,34,17,0,95,102,3,32,16,0,96,102,3,54,27,0,97,102,3,44,22,0,
        98,102,3,52,26,0,99,102,3,56,28,0,100,102,3,64,32,0,101,88,1,0,0,
        0,101,89,1,0,0,0,101,90,1,0,0,0,101,91,1,0,0,0,101,92,1,0,0,0,101,
        93,1,0,0,0,101,94,1,0,0,0,101,95,1,0,0,0,101,96,1,0,0,0,101,97,1,
        0,0,0,101,98,1,0,0,0,101,99,1,0,0,0,101,100,1,0,0,0,102,3,1,0,0,
        0,103,113,3,42,21,0,104,113,3,6,3,0,105,113,3,66,33,0,106,113,3,
        26,13,0,107,113,3,32,16,0,108,113,3,40,20,0,109,113,3,56,28,0,110,
        113,5,16,0,0,111,113,3,54,27,0,112,103,1,0,0,0,112,104,1,0,0,0,112,
        105,1,0,0,0,112,106,1,0,0,0,112,107,1,0,0,0,112,108,1,0,0,0,112,
        109,1,0,0,0,112,110,1,0,0,0,112,111,1,0,0,0,113,5,1,0,0,0,114,116,
        5,7,0,0,115,114,1,0,0,0,115,116,1,0,0,0,116,119,1,0,0,0,117,120,
        3,22,11,0,118,120,5,68,0,0,119,117,1,0,0,0,119,118,1,0,0,0,120,121,
        1,0,0,0,121,122,5,8,0,0,122,124,3,20,10,0,123,125,3,24,12,0,124,
        123,1,0,0,0,124,125,1,0,0,0,125,7,1,0,0,0,126,128,5,18,0,0,127,126,
        1,0,0,0,127,128,1,0,0,0,128,129,1,0,0,0,129,131,3,10,5,0,130,132,
        5,19,0,0,131,130,1,0,0,0,131,132,1,0,0,0,132,9,1,0,0,0,133,136,5,
        68,0,0,134,136,3,12,6,0,135,133,1,0,0,0,135,134,1,0,0,0,136,11,1,
        0,0,0,137,138,5,47,0,0,138,143,3,14,7,0,139,140,5,42,0,0,140,142,
        3,14,7,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,
        1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,147,5,48,0,0,147,13,
        1,0,0,0,148,153,3,16,8,0,149,150,5,43,0,0,150,152,3,16,8,0,151,149,
        1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,15,1,
        0,0,0,155,153,1,0,0,0,156,157,7,0,0,0,157,17,1,0,0,0,158,163,7,1,
        0,0,159,160,5,22,0,0,160,162,7,1,0,0,161,159,1,0,0,0,162,165,1,0,
        0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,19,1,0,0,0,165,163,1,0,0,
        0,166,181,3,34,17,0,167,181,3,38,19,0,168,181,3,58,29,0,169,181,
        3,68,34,0,170,181,3,8,4,0,171,181,3,18,9,0,172,181,5,53,0,0,173,
        181,5,54,0,0,174,181,3,22,11,0,175,181,5,68,0,0,176,177,5,51,0,0,
        177,178,3,20,10,0,178,179,5,52,0,0,179,181,1,0,0,0,180,166,1,0,0,
        0,180,167,1,0,0,0,180,168,1,0,0,0,180,169,1,0,0,0,180,170,1,0,0,
        0,180,171,1,0,0,0,180,172,1,0,0,0,180,173,1,0,0,0,180,174,1,0,0,
        0,180,175,1,0,0,0,180,176,1,0,0,0,181,21,1,0,0,0,182,183,5,20,0,
        0,183,185,5,21,0,0,184,182,1,0,0,0,185,186,1,0,0,0,186,184,1,0,0,
        0,186,187,1,0,0,0,187,188,1,0,0,0,188,189,5,68,0,0,189,23,1,0,0,
        0,190,191,7,2,0,0,191,25,1,0,0,0,192,193,5,3,0,0,193,194,5,68,0,
        0,194,196,5,51,0,0,195,197,3,28,14,0,196,195,1,0,0,0,196,197,1,0,
        0,0,197,198,1,0,0,0,198,199,5,52,0,0,199,200,3,56,28,0,200,201,5,
        4,0,0,201,27,1,0,0,0,202,207,3,30,15,0,203,204,5,43,0,0,204,206,
        3,30,15,0,205,203,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,
        1,0,0,0,208,29,1,0,0,0,209,207,1,0,0,0,210,212,5,68,0,0,211,213,
        3,24,12,0,212,211,1,0,0,0,212,213,1,0,0,0,213,31,1,0,0,0,214,215,
        5,5,0,0,215,216,3,20,10,0,216,33,1,0,0,0,217,219,5,6,0,0,218,217,
        1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,221,5,68,0,0,221,223,
        5,51,0,0,222,224,3,36,18,0,223,222,1,0,0,0,223,224,1,0,0,0,224,225,
        1,0,0,0,225,226,5,52,0,0,226,35,1,0,0,0,227,232,3,20,10,0,228,229,
        5,43,0,0,229,231,3,20,10,0,230,228,1,0,0,0,231,234,1,0,0,0,232,230,
        1,0,0,0,232,233,1,0,0,0,233,37,1,0,0,0,234,232,1,0,0,0,235,236,5,
        63,0,0,236,237,5,51,0,0,237,238,3,58,29,0,238,239,5,43,0,0,239,240,
        3,58,29,0,240,241,5,52,0,0,241,248,1,0,0,0,242,243,7,3,0,0,243,244,
        5,51,0,0,244,245,3,58,29,0,245,246,5,52,0,0,246,248,1,0,0,0,247,
        235,1,0,0,0,247,242,1,0,0,0,248,39,1,0,0,0,249,250,5,10,0,0,250,
        251,5,51,0,0,251,252,3,68,34,0,252,255,5,52,0,0,253,256,3,2,1,0,
        254,256,3,56,28,0,255,253,1,0,0,0,255,254,1,0,0,0,256,267,1,0,0,
        0,257,258,5,11,0,0,258,259,5,51,0,0,259,260,3,68,34,0,260,263,5,
        52,0,0,261,264,3,2,1,0,262,264,3,56,28,0,263,261,1,0,0,0,263,262,
        1,0,0,0,264,266,1,0,0,0,265,257,1,0,0,0,266,269,1,0,0,0,267,265,
        1,0,0,0,267,268,1,0,0,0,268,275,1,0,0,0,269,267,1,0,0,0,270,273,
        5,12,0,0,271,274,3,2,1,0,272,274,3,56,28,0,273,271,1,0,0,0,273,272,
        1,0,0,0,274,276,1,0,0,0,275,270,1,0,0,0,275,276,1,0,0,0,276,41,1,
        0,0,0,277,280,3,44,22,0,278,280,3,52,26,0,279,277,1,0,0,0,279,278,
        1,0,0,0,280,43,1,0,0,0,281,282,5,13,0,0,282,284,5,51,0,0,283,285,
        3,46,23,0,284,283,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,287,
        5,42,0,0,287,288,3,68,34,0,288,289,5,42,0,0,289,290,3,48,24,0,290,
        291,5,52,0,0,291,292,3,50,25,0,292,45,1,0,0,0,293,296,5,68,0,0,294,
        296,3,6,3,0,295,293,1,0,0,0,295,294,1,0,0,0,296,47,1,0,0,0,297,301,
        3,6,3,0,298,301,3,66,33,0,299,301,3,64,32,0,300,297,1,0,0,0,300,
        298,1,0,0,0,300,299,1,0,0,0,301,49,1,0,0,0,302,304,5,49,0,0,303,
        305,3,4,2,0,304,303,1,0,0,0,305,306,1,0,0,0,306,304,1,0,0,0,306,
        307,1,0,0,0,307,308,1,0,0,0,308,309,5,50,0,0,309,312,1,0,0,0,310,
        312,3,2,1,0,311,302,1,0,0,0,311,310,1,0,0,0,312,51,1,0,0,0,313,314,
        5,17,0,0,314,315,5,51,0,0,315,316,3,68,34,0,316,326,5,52,0,0,317,
        319,5,49,0,0,318,320,3,4,2,0,319,318,1,0,0,0,320,321,1,0,0,0,321,
        319,1,0,0,0,321,322,1,0,0,0,322,323,1,0,0,0,323,324,5,50,0,0,324,
        327,1,0,0,0,325,327,3,2,1,0,326,317,1,0,0,0,326,325,1,0,0,0,327,
        53,1,0,0,0,328,329,5,9,0,0,329,334,3,20,10,0,330,331,5,43,0,0,331,
        333,3,20,10,0,332,330,1,0,0,0,333,336,1,0,0,0,334,332,1,0,0,0,334,
        335,1,0,0,0,335,55,1,0,0,0,336,334,1,0,0,0,337,341,5,49,0,0,338,
        340,3,2,1,0,339,338,1,0,0,0,340,343,1,0,0,0,341,339,1,0,0,0,341,
        342,1,0,0,0,342,344,1,0,0,0,343,341,1,0,0,0,344,345,5,50,0,0,345,
        57,1,0,0,0,346,347,6,29,-1,0,347,348,3,60,30,0,348,354,1,0,0,0,349,
        350,10,2,0,0,350,351,7,4,0,0,351,353,3,60,30,0,352,349,1,0,0,0,353,
        356,1,0,0,0,354,352,1,0,0,0,354,355,1,0,0,0,355,59,1,0,0,0,356,354,
        1,0,0,0,357,358,6,30,-1,0,358,359,3,62,31,0,359,365,1,0,0,0,360,
        361,10,2,0,0,361,362,7,5,0,0,362,364,3,62,31,0,363,360,1,0,0,0,364,
        367,1,0,0,0,365,363,1,0,0,0,365,366,1,0,0,0,366,61,1,0,0,0,367,365,
        1,0,0,0,368,369,5,22,0,0,369,388,3,62,31,0,370,371,5,23,0,0,371,
        388,3,62,31,0,372,388,3,34,17,0,373,388,5,53,0,0,374,388,3,22,11,
        0,375,388,5,68,0,0,376,388,5,54,0,0,377,388,3,64,32,0,378,379,5,
        51,0,0,379,380,3,58,29,0,380,381,5,52,0,0,381,388,1,0,0,0,382,383,
        5,51,0,0,383,384,3,24,12,0,384,385,5,52,0,0,385,386,3,62,31,0,386,
        388,1,0,0,0,387,368,1,0,0,0,387,370,1,0,0,0,387,372,1,0,0,0,387,
        373,1,0,0,0,387,374,1,0,0,0,387,375,1,0,0,0,387,376,1,0,0,0,387,
        377,1,0,0,0,387,378,1,0,0,0,387,382,1,0,0,0,388,63,1,0,0,0,389,390,
        5,68,0,0,390,392,7,6,0,0,391,393,5,42,0,0,392,391,1,0,0,0,392,393,
        1,0,0,0,393,65,1,0,0,0,394,397,3,22,11,0,395,397,5,68,0,0,396,394,
        1,0,0,0,396,395,1,0,0,0,397,410,1,0,0,0,398,399,5,32,0,0,399,403,
        5,54,0,0,400,401,5,32,0,0,401,403,3,58,29,0,402,398,1,0,0,0,402,
        400,1,0,0,0,403,411,1,0,0,0,404,405,5,33,0,0,405,411,3,58,29,0,406,
        407,5,37,0,0,407,411,3,58,29,0,408,409,5,36,0,0,409,411,3,58,29,
        0,410,402,1,0,0,0,410,404,1,0,0,0,410,406,1,0,0,0,410,408,1,0,0,
        0,411,412,1,0,0,0,412,413,5,42,0,0,413,67,1,0,0,0,414,415,3,70,35,
        0,415,69,1,0,0,0,416,421,3,72,36,0,417,418,5,40,0,0,418,420,3,72,
        36,0,419,417,1,0,0,0,420,423,1,0,0,0,421,419,1,0,0,0,421,422,1,0,
        0,0,422,71,1,0,0,0,423,421,1,0,0,0,424,429,3,74,37,0,425,426,5,39,
        0,0,426,428,3,74,37,0,427,425,1,0,0,0,428,431,1,0,0,0,429,427,1,
        0,0,0,429,430,1,0,0,0,430,73,1,0,0,0,431,429,1,0,0,0,432,433,5,41,
        0,0,433,436,3,74,37,0,434,436,3,76,38,0,435,432,1,0,0,0,435,434,
        1,0,0,0,436,75,1,0,0,0,437,438,3,58,29,0,438,439,3,78,39,0,439,440,
        3,58,29,0,440,457,1,0,0,0,441,442,3,18,9,0,442,443,7,7,0,0,443,444,
        3,18,9,0,444,457,1,0,0,0,445,446,3,8,4,0,446,447,7,7,0,0,447,448,
        3,8,4,0,448,457,1,0,0,0,449,450,5,51,0,0,450,451,3,68,34,0,451,452,
        5,52,0,0,452,457,1,0,0,0,453,457,5,61,0,0,454,457,5,62,0,0,455,457,
        5,68,0,0,456,437,1,0,0,0,456,441,1,0,0,0,456,445,1,0,0,0,456,449,
        1,0,0,0,456,453,1,0,0,0,456,454,1,0,0,0,456,455,1,0,0,0,457,77,1,
        0,0,0,458,459,7,8,0,0,459,79,1,0,0,0,47,84,101,112,115,119,124,127,
        131,135,143,153,163,180,186,196,207,212,218,223,232,247,255,263,
        267,273,275,279,284,295,300,306,311,321,326,334,341,354,365,387,
        392,396,402,410,421,429,435,456
    ]

class AingalLangParser ( Parser ):

    grammarFileName = "AingalLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Start Program'", "'End Program'", "'Define Function'", 
                     "'End Function'", "'Return'", "'Call'", "'Set'", "'to'", 
                     "'Display'", "'if'", "'else if'", "'else'", "'For'", 
                     "'from'", "'in'", "'break'", "'While'", "'invert'", 
                     "''T'", "'parent'", "'::'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'>'", "'<'", "'>='", "'<='", "'+='", 
                     "'-='", "'++'", "'--'", "'*='", "'/='", "'!='", "'and'", 
                     "'or'", "'not'", "';'", "','", "':'", "'.'", "'\"'", 
                     "'['", "']'", "'{'", "'}'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "'int'", "'string'", "'bool'", "'float'", 
                     "'matrix'", "'void'", "'true'", "'false'", "'pow'", 
                     "'sin'", "'cos'", "'tan'", "'ctan'" ]

    symbolicNames = [ "<INVALID>", "START_PROGRAM", "END_PROGRAM", "DEFINE_FUNCTION", 
                      "END_FUNCTION", "RETURN", "CALL", "SET", "TO", "DISPLAY", 
                      "IF", "ELSE_IF", "ELSE", "FOR", "FROM", "IN", "BREAK", 
                      "WHILE", "INVERT_MATRIX", "TRANSPOSITION", "PARENT_SCOPE", 
                      "DCOLON", "PLUS", "MINUS", "MULTIPLY", "DIVIDED_BY", 
                      "MODULO", "EQUALS", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
                      "LESS_EQUAL", "ADD_TO", "SUBTRACT_FROM", "INCREMENT", 
                      "DECREMENT", "TIMES", "DIVIDE_FROM", "NOT_EQUALS", 
                      "AND", "OR", "NOT", "SEMICOLON", "COMMA", "COLON", 
                      "DOT", "QUOTE", "LBRACK", "RBRACK", "LBRACE", "RBRACE", 
                      "LPAREN", "RPAREN", "NUMBER", "STRING", "TYPE_INT", 
                      "TYPE_STRING", "TYPE_BOOL", "TYPE_FLOAT", "TYPE_MATRIX", 
                      "TYPE_VOID", "TRUE_VALUE", "FALSE_VALUE", "POWER_FUNC", 
                      "SIN_FUNC", "COS_FUNC", "TAN_FUNC", "CTAN_FUNC", "IDENTIFIER", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_loopStatements = 2
    RULE_variableDeclaration = 3
    RULE_matrixExpression = 4
    RULE_matrixAtom = 5
    RULE_matrixConstruction = 6
    RULE_row = 7
    RULE_value = 8
    RULE_stringExpression = 9
    RULE_expression = 10
    RULE_scopedIdentifier = 11
    RULE_typeAnnotation = 12
    RULE_functionDeclaration = 13
    RULE_parameter = 14
    RULE_typedParameter = 15
    RULE_returnStatement = 16
    RULE_functionCall = 17
    RULE_argumentList = 18
    RULE_builtInFunctions = 19
    RULE_ifStatement = 20
    RULE_loopStatement = 21
    RULE_forLoop = 22
    RULE_forInit = 23
    RULE_forUpdate = 24
    RULE_forBody = 25
    RULE_whileLoop = 26
    RULE_displayStatement = 27
    RULE_blockStatement = 28
    RULE_numExpression = 29
    RULE_term = 30
    RULE_factor = 31
    RULE_operation = 32
    RULE_reassignment = 33
    RULE_boolExpression = 34
    RULE_boolOrExpression = 35
    RULE_boolAndExpression = 36
    RULE_boolNotExpression = 37
    RULE_boolPrimary = 38
    RULE_comparisonOp = 39

    ruleNames =  [ "program", "statement", "loopStatements", "variableDeclaration", 
                   "matrixExpression", "matrixAtom", "matrixConstruction", 
                   "row", "value", "stringExpression", "expression", "scopedIdentifier", 
                   "typeAnnotation", "functionDeclaration", "parameter", 
                   "typedParameter", "returnStatement", "functionCall", 
                   "argumentList", "builtInFunctions", "ifStatement", "loopStatement", 
                   "forLoop", "forInit", "forUpdate", "forBody", "whileLoop", 
                   "displayStatement", "blockStatement", "numExpression", 
                   "term", "factor", "operation", "reassignment", "boolExpression", 
                   "boolOrExpression", "boolAndExpression", "boolNotExpression", 
                   "boolPrimary", "comparisonOp" ]

    EOF = Token.EOF
    START_PROGRAM=1
    END_PROGRAM=2
    DEFINE_FUNCTION=3
    END_FUNCTION=4
    RETURN=5
    CALL=6
    SET=7
    TO=8
    DISPLAY=9
    IF=10
    ELSE_IF=11
    ELSE=12
    FOR=13
    FROM=14
    IN=15
    BREAK=16
    WHILE=17
    INVERT_MATRIX=18
    TRANSPOSITION=19
    PARENT_SCOPE=20
    DCOLON=21
    PLUS=22
    MINUS=23
    MULTIPLY=24
    DIVIDED_BY=25
    MODULO=26
    EQUALS=27
    GREATER_THAN=28
    LESS_THAN=29
    GREATER_EQUAL=30
    LESS_EQUAL=31
    ADD_TO=32
    SUBTRACT_FROM=33
    INCREMENT=34
    DECREMENT=35
    TIMES=36
    DIVIDE_FROM=37
    NOT_EQUALS=38
    AND=39
    OR=40
    NOT=41
    SEMICOLON=42
    COMMA=43
    COLON=44
    DOT=45
    QUOTE=46
    LBRACK=47
    RBRACK=48
    LBRACE=49
    RBRACE=50
    LPAREN=51
    RPAREN=52
    NUMBER=53
    STRING=54
    TYPE_INT=55
    TYPE_STRING=56
    TYPE_BOOL=57
    TYPE_FLOAT=58
    TYPE_MATRIX=59
    TYPE_VOID=60
    TRUE_VALUE=61
    FALSE_VALUE=62
    POWER_FUNC=63
    SIN_FUNC=64
    COS_FUNC=65
    TAN_FUNC=66
    CTAN_FUNC=67
    IDENTIFIER=68
    WS=69
    COMMENT=70

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START_PROGRAM(self):
            return self.getToken(AingalLangParser.START_PROGRAM, 0)

        def END_PROGRAM(self):
            return self.getToken(AingalLangParser.END_PROGRAM, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.StatementContext,i)


        def getRuleIndex(self):
            return AingalLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AingalLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(AingalLangParser.START_PROGRAM)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.statement()
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 562949954610920) != 0) or _la==68):
                    break

            self.state = 86
            self.match(AingalLangParser.END_PROGRAM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(AingalLangParser.FunctionCallContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(AingalLangParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(AingalLangParser.LoopStatementContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(AingalLangParser.VariableDeclarationContext,0)


        def reassignment(self):
            return self.getTypedRuleContext(AingalLangParser.ReassignmentContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(AingalLangParser.FunctionDeclarationContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(AingalLangParser.ReturnStatementContext,0)


        def displayStatement(self):
            return self.getTypedRuleContext(AingalLangParser.DisplayStatementContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(AingalLangParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(AingalLangParser.WhileLoopContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(AingalLangParser.BlockStatementContext,0)


        def operation(self):
            return self.getTypedRuleContext(AingalLangParser.OperationContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = AingalLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.functionCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.loopStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.variableDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.reassignment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 93
                self.functionDeclaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 94
                self.functionCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 95
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 96
                self.displayStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 97
                self.forLoop()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 98
                self.whileLoop()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 99
                self.blockStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 100
                self.operation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loopStatement(self):
            return self.getTypedRuleContext(AingalLangParser.LoopStatementContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(AingalLangParser.VariableDeclarationContext,0)


        def reassignment(self):
            return self.getTypedRuleContext(AingalLangParser.ReassignmentContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(AingalLangParser.FunctionDeclarationContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(AingalLangParser.ReturnStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(AingalLangParser.IfStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(AingalLangParser.BlockStatementContext,0)


        def BREAK(self):
            return self.getToken(AingalLangParser.BREAK, 0)

        def displayStatement(self):
            return self.getTypedRuleContext(AingalLangParser.DisplayStatementContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_loopStatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatements" ):
                listener.enterLoopStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatements" ):
                listener.exitLoopStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatements" ):
                return visitor.visitLoopStatements(self)
            else:
                return visitor.visitChildren(self)




    def loopStatements(self):

        localctx = AingalLangParser.LoopStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loopStatements)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.loopStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.variableDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.reassignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.functionDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.returnStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 109
                self.blockStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 110
                self.match(AingalLangParser.BREAK)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 111
                self.displayStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TO(self):
            return self.getToken(AingalLangParser.TO, 0)

        def expression(self):
            return self.getTypedRuleContext(AingalLangParser.ExpressionContext,0)


        def scopedIdentifier(self):
            return self.getTypedRuleContext(AingalLangParser.ScopedIdentifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def SET(self):
            return self.getToken(AingalLangParser.SET, 0)

        def typeAnnotation(self):
            return self.getTypedRuleContext(AingalLangParser.TypeAnnotationContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = AingalLangParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 114
                self.match(AingalLangParser.SET)


            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 117
                self.scopedIdentifier()
                pass
            elif token in [68]:
                self.state = 118
                self.match(AingalLangParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 121
            self.match(AingalLangParser.TO)
            self.state = 122
            self.expression()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1116892707587883008) != 0):
                self.state = 123
                self.typeAnnotation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matrixAtom(self):
            return self.getTypedRuleContext(AingalLangParser.MatrixAtomContext,0)


        def INVERT_MATRIX(self):
            return self.getToken(AingalLangParser.INVERT_MATRIX, 0)

        def TRANSPOSITION(self):
            return self.getToken(AingalLangParser.TRANSPOSITION, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_matrixExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixExpression" ):
                listener.enterMatrixExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixExpression" ):
                listener.exitMatrixExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixExpression" ):
                return visitor.visitMatrixExpression(self)
            else:
                return visitor.visitChildren(self)




    def matrixExpression(self):

        localctx = AingalLangParser.MatrixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_matrixExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 126
                self.match(AingalLangParser.INVERT_MATRIX)


            self.state = 129
            self.matrixAtom()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 130
                self.match(AingalLangParser.TRANSPOSITION)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def matrixConstruction(self):
            return self.getTypedRuleContext(AingalLangParser.MatrixConstructionContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_matrixAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixAtom" ):
                listener.enterMatrixAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixAtom" ):
                listener.exitMatrixAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixAtom" ):
                return visitor.visitMatrixAtom(self)
            else:
                return visitor.visitChildren(self)




    def matrixAtom(self):

        localctx = AingalLangParser.MatrixAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_matrixAtom)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [68]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(AingalLangParser.IDENTIFIER)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.matrixConstruction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixConstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(AingalLangParser.LBRACK, 0)

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.RowContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.RowContext,i)


        def RBRACK(self):
            return self.getToken(AingalLangParser.RBRACK, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.SEMICOLON)
            else:
                return self.getToken(AingalLangParser.SEMICOLON, i)

        def getRuleIndex(self):
            return AingalLangParser.RULE_matrixConstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixConstruction" ):
                listener.enterMatrixConstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixConstruction" ):
                listener.exitMatrixConstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixConstruction" ):
                return visitor.visitMatrixConstruction(self)
            else:
                return visitor.visitChildren(self)




    def matrixConstruction(self):

        localctx = AingalLangParser.MatrixConstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_matrixConstruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(AingalLangParser.LBRACK)
            self.state = 138
            self.row()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 139
                self.match(AingalLangParser.SEMICOLON)
                self.state = 140
                self.row()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(AingalLangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.ValueContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.COMMA)
            else:
                return self.getToken(AingalLangParser.COMMA, i)

        def getRuleIndex(self):
            return AingalLangParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow" ):
                return visitor.visitRow(self)
            else:
                return visitor.visitChildren(self)




    def row(self):

        localctx = AingalLangParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.value()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 149
                self.match(AingalLangParser.COMMA)
                self.state = 150
                self.value()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AingalLangParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = AingalLangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not(_la==53 or _la==68):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.STRING)
            else:
                return self.getToken(AingalLangParser.STRING, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.IDENTIFIER)
            else:
                return self.getToken(AingalLangParser.IDENTIFIER, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.PLUS)
            else:
                return self.getToken(AingalLangParser.PLUS, i)

        def getRuleIndex(self):
            return AingalLangParser.RULE_stringExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpression" ):
                listener.enterStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpression" ):
                listener.exitStringExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpression" ):
                return visitor.visitStringExpression(self)
            else:
                return visitor.visitChildren(self)




    def stringExpression(self):

        localctx = AingalLangParser.StringExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stringExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not(_la==54 or _la==68):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 159
                self.match(AingalLangParser.PLUS)
                self.state = 160
                _la = self._input.LA(1)
                if not(_la==54 or _la==68):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(AingalLangParser.FunctionCallContext,0)


        def builtInFunctions(self):
            return self.getTypedRuleContext(AingalLangParser.BuiltInFunctionsContext,0)


        def numExpression(self):
            return self.getTypedRuleContext(AingalLangParser.NumExpressionContext,0)


        def boolExpression(self):
            return self.getTypedRuleContext(AingalLangParser.BoolExpressionContext,0)


        def matrixExpression(self):
            return self.getTypedRuleContext(AingalLangParser.MatrixExpressionContext,0)


        def stringExpression(self):
            return self.getTypedRuleContext(AingalLangParser.StringExpressionContext,0)


        def NUMBER(self):
            return self.getToken(AingalLangParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(AingalLangParser.STRING, 0)

        def scopedIdentifier(self):
            return self.getTypedRuleContext(AingalLangParser.ScopedIdentifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(AingalLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(AingalLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(AingalLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = AingalLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.functionCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.builtInFunctions()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.numExpression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 169
                self.boolExpression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 170
                self.matrixExpression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 171
                self.stringExpression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 172
                self.match(AingalLangParser.NUMBER)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 173
                self.match(AingalLangParser.STRING)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 174
                self.scopedIdentifier()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 175
                self.match(AingalLangParser.IDENTIFIER)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 176
                self.match(AingalLangParser.LPAREN)
                self.state = 177
                self.expression()
                self.state = 178
                self.match(AingalLangParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopedIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def PARENT_SCOPE(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.PARENT_SCOPE)
            else:
                return self.getToken(AingalLangParser.PARENT_SCOPE, i)

        def DCOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.DCOLON)
            else:
                return self.getToken(AingalLangParser.DCOLON, i)

        def getRuleIndex(self):
            return AingalLangParser.RULE_scopedIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScopedIdentifier" ):
                listener.enterScopedIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScopedIdentifier" ):
                listener.exitScopedIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScopedIdentifier" ):
                return visitor.visitScopedIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def scopedIdentifier(self):

        localctx = AingalLangParser.ScopedIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_scopedIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 182
                self.match(AingalLangParser.PARENT_SCOPE)
                self.state = 183
                self.match(AingalLangParser.DCOLON)
                self.state = 186 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

            self.state = 188
            self.match(AingalLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeAnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_STRING(self):
            return self.getToken(AingalLangParser.TYPE_STRING, 0)

        def TYPE_INT(self):
            return self.getToken(AingalLangParser.TYPE_INT, 0)

        def TYPE_FLOAT(self):
            return self.getToken(AingalLangParser.TYPE_FLOAT, 0)

        def TYPE_BOOL(self):
            return self.getToken(AingalLangParser.TYPE_BOOL, 0)

        def TYPE_MATRIX(self):
            return self.getToken(AingalLangParser.TYPE_MATRIX, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_typeAnnotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAnnotation" ):
                listener.enterTypeAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAnnotation" ):
                listener.exitTypeAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAnnotation" ):
                return visitor.visitTypeAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def typeAnnotation(self):

        localctx = AingalLangParser.TypeAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_typeAnnotation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1116892707587883008) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE_FUNCTION(self):
            return self.getToken(AingalLangParser.DEFINE_FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(AingalLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AingalLangParser.RPAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(AingalLangParser.BlockStatementContext,0)


        def END_FUNCTION(self):
            return self.getToken(AingalLangParser.END_FUNCTION, 0)

        def parameter(self):
            return self.getTypedRuleContext(AingalLangParser.ParameterContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = AingalLangParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(AingalLangParser.DEFINE_FUNCTION)
            self.state = 193
            self.match(AingalLangParser.IDENTIFIER)
            self.state = 194
            self.match(AingalLangParser.LPAREN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==68:
                self.state = 195
                self.parameter()


            self.state = 198
            self.match(AingalLangParser.RPAREN)
            self.state = 199
            self.blockStatement()
            self.state = 200
            self.match(AingalLangParser.END_FUNCTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.TypedParameterContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.TypedParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.COMMA)
            else:
                return self.getToken(AingalLangParser.COMMA, i)

        def getRuleIndex(self):
            return AingalLangParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = AingalLangParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.typedParameter()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 203
                self.match(AingalLangParser.COMMA)
                self.state = 204
                self.typedParameter()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def typeAnnotation(self):
            return self.getTypedRuleContext(AingalLangParser.TypeAnnotationContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_typedParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedParameter" ):
                listener.enterTypedParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedParameter" ):
                listener.exitTypedParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedParameter" ):
                return visitor.visitTypedParameter(self)
            else:
                return visitor.visitChildren(self)




    def typedParameter(self):

        localctx = AingalLangParser.TypedParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_typedParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(AingalLangParser.IDENTIFIER)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1116892707587883008) != 0):
                self.state = 211
                self.typeAnnotation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(AingalLangParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(AingalLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = AingalLangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(AingalLangParser.RETURN)
            self.state = 215
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(AingalLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AingalLangParser.RPAREN, 0)

        def CALL(self):
            return self.getToken(AingalLangParser.CALL, 0)

        def argumentList(self):
            return self.getTypedRuleContext(AingalLangParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = AingalLangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 217
                self.match(AingalLangParser.CALL)


            self.state = 220
            self.match(AingalLangParser.IDENTIFIER)
            self.state = 221
            self.match(AingalLangParser.LPAREN)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 6)) & ~0x3f) == 0 and ((1 << (_la - 6)) & 9187802870056177665) != 0):
                self.state = 222
                self.argumentList()


            self.state = 225
            self.match(AingalLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.COMMA)
            else:
                return self.getToken(AingalLangParser.COMMA, i)

        def getRuleIndex(self):
            return AingalLangParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = AingalLangParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.expression()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 228
                self.match(AingalLangParser.COMMA)
                self.state = 229
                self.expression()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuiltInFunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POWER_FUNC(self):
            return self.getToken(AingalLangParser.POWER_FUNC, 0)

        def LPAREN(self):
            return self.getToken(AingalLangParser.LPAREN, 0)

        def numExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.NumExpressionContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.NumExpressionContext,i)


        def COMMA(self):
            return self.getToken(AingalLangParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(AingalLangParser.RPAREN, 0)

        def SIN_FUNC(self):
            return self.getToken(AingalLangParser.SIN_FUNC, 0)

        def COS_FUNC(self):
            return self.getToken(AingalLangParser.COS_FUNC, 0)

        def TAN_FUNC(self):
            return self.getToken(AingalLangParser.TAN_FUNC, 0)

        def CTAN_FUNC(self):
            return self.getToken(AingalLangParser.CTAN_FUNC, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_builtInFunctions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuiltInFunctions" ):
                listener.enterBuiltInFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuiltInFunctions" ):
                listener.exitBuiltInFunctions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuiltInFunctions" ):
                return visitor.visitBuiltInFunctions(self)
            else:
                return visitor.visitChildren(self)




    def builtInFunctions(self):

        localctx = AingalLangParser.BuiltInFunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_builtInFunctions)
        self._la = 0 # Token type
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(AingalLangParser.POWER_FUNC)
                self.state = 236
                self.match(AingalLangParser.LPAREN)
                self.state = 237
                self.numExpression(0)
                self.state = 238
                self.match(AingalLangParser.COMMA)
                self.state = 239
                self.numExpression(0)
                self.state = 240
                self.match(AingalLangParser.RPAREN)
                pass
            elif token in [64, 65, 66, 67]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                _la = self._input.LA(1)
                if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 15) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 243
                self.match(AingalLangParser.LPAREN)
                self.state = 244
                self.numExpression(0)
                self.state = 245
                self.match(AingalLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(AingalLangParser.IF, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.LPAREN)
            else:
                return self.getToken(AingalLangParser.LPAREN, i)

        def boolExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.BoolExpressionContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.BoolExpressionContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.RPAREN)
            else:
                return self.getToken(AingalLangParser.RPAREN, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.StatementContext,i)


        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.BlockStatementContext,i)


        def ELSE_IF(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.ELSE_IF)
            else:
                return self.getToken(AingalLangParser.ELSE_IF, i)

        def ELSE(self):
            return self.getToken(AingalLangParser.ELSE, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = AingalLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(AingalLangParser.IF)
            self.state = 250
            self.match(AingalLangParser.LPAREN)
            self.state = 251
            self.boolExpression()
            self.state = 252
            self.match(AingalLangParser.RPAREN)
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 253
                self.statement()
                pass

            elif la_ == 2:
                self.state = 254
                self.blockStatement()
                pass


            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 257
                    self.match(AingalLangParser.ELSE_IF)
                    self.state = 258
                    self.match(AingalLangParser.LPAREN)
                    self.state = 259
                    self.boolExpression()
                    self.state = 260
                    self.match(AingalLangParser.RPAREN)
                    self.state = 263
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        self.state = 261
                        self.statement()
                        pass

                    elif la_ == 2:
                        self.state = 262
                        self.blockStatement()
                        pass

             
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 270
                self.match(AingalLangParser.ELSE)
                self.state = 273
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 271
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 272
                    self.blockStatement()
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forLoop(self):
            return self.getTypedRuleContext(AingalLangParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(AingalLangParser.WhileLoopContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = AingalLangParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_loopStatement)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.forLoop()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.whileLoop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cond = None # BoolExpressionContext

        def FOR(self):
            return self.getToken(AingalLangParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(AingalLangParser.LPAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.SEMICOLON)
            else:
                return self.getToken(AingalLangParser.SEMICOLON, i)

        def forUpdate(self):
            return self.getTypedRuleContext(AingalLangParser.ForUpdateContext,0)


        def RPAREN(self):
            return self.getToken(AingalLangParser.RPAREN, 0)

        def forBody(self):
            return self.getTypedRuleContext(AingalLangParser.ForBodyContext,0)


        def boolExpression(self):
            return self.getTypedRuleContext(AingalLangParser.BoolExpressionContext,0)


        def forInit(self):
            return self.getTypedRuleContext(AingalLangParser.ForInitContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = AingalLangParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(AingalLangParser.FOR)
            self.state = 282
            self.match(AingalLangParser.LPAREN)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & 2305843009213702145) != 0):
                self.state = 283
                self.forInit()


            self.state = 286
            self.match(AingalLangParser.SEMICOLON)
            self.state = 287
            localctx.cond = self.boolExpression()
            self.state = 288
            self.match(AingalLangParser.SEMICOLON)
            self.state = 289
            self.forUpdate()
            self.state = 290
            self.match(AingalLangParser.RPAREN)
            self.state = 291
            self.forBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def variableDeclaration(self):
            return self.getTypedRuleContext(AingalLangParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = AingalLangParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forInit)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(AingalLangParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.variableDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(AingalLangParser.VariableDeclarationContext,0)


        def reassignment(self):
            return self.getTypedRuleContext(AingalLangParser.ReassignmentContext,0)


        def operation(self):
            return self.getTypedRuleContext(AingalLangParser.OperationContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = AingalLangParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forUpdate)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.reassignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 299
                self.operation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(AingalLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AingalLangParser.RBRACE, 0)

        def loopStatements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.LoopStatementsContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.LoopStatementsContext,i)


        def statement(self):
            return self.getTypedRuleContext(AingalLangParser.StatementContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_forBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForBody" ):
                listener.enterForBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForBody" ):
                listener.exitForBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForBody" ):
                return visitor.visitForBody(self)
            else:
                return visitor.visitChildren(self)




    def forBody(self):

        localctx = AingalLangParser.ForBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forBody)
        self._la = 0 # Token type
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(AingalLangParser.LBRACE)
                self.state = 304 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 303
                    self.loopStatements()
                    self.state = 306 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 562949954676392) != 0) or _la==68):
                        break

                self.state = 308
                self.match(AingalLangParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(AingalLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(AingalLangParser.LPAREN, 0)

        def boolExpression(self):
            return self.getTypedRuleContext(AingalLangParser.BoolExpressionContext,0)


        def RPAREN(self):
            return self.getToken(AingalLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(AingalLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AingalLangParser.RBRACE, 0)

        def statement(self):
            return self.getTypedRuleContext(AingalLangParser.StatementContext,0)


        def loopStatements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.LoopStatementsContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.LoopStatementsContext,i)


        def getRuleIndex(self):
            return AingalLangParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = AingalLangParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(AingalLangParser.WHILE)
            self.state = 314
            self.match(AingalLangParser.LPAREN)
            self.state = 315
            self.boolExpression()
            self.state = 316
            self.match(AingalLangParser.RPAREN)
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 317
                self.match(AingalLangParser.LBRACE)
                self.state = 319 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 318
                    self.loopStatements()
                    self.state = 321 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 562949954676392) != 0) or _la==68):
                        break

                self.state = 323
                self.match(AingalLangParser.RBRACE)
                pass

            elif la_ == 2:
                self.state = 325
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISPLAY(self):
            return self.getToken(AingalLangParser.DISPLAY, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.COMMA)
            else:
                return self.getToken(AingalLangParser.COMMA, i)

        def getRuleIndex(self):
            return AingalLangParser.RULE_displayStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayStatement" ):
                listener.enterDisplayStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayStatement" ):
                listener.exitDisplayStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplayStatement" ):
                return visitor.visitDisplayStatement(self)
            else:
                return visitor.visitChildren(self)




    def displayStatement(self):

        localctx = AingalLangParser.DisplayStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_displayStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(AingalLangParser.DISPLAY)
            self.state = 329
            self.expression()
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 330
                self.match(AingalLangParser.COMMA)
                self.state = 331
                self.expression()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(AingalLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AingalLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.StatementContext,i)


        def getRuleIndex(self):
            return AingalLangParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = AingalLangParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(AingalLangParser.LBRACE)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949954610920) != 0) or _la==68:
                self.state = 338
                self.statement()
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 344
            self.match(AingalLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(AingalLangParser.TermContext,0)


        def numExpression(self):
            return self.getTypedRuleContext(AingalLangParser.NumExpressionContext,0)


        def PLUS(self):
            return self.getToken(AingalLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(AingalLangParser.MINUS, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_numExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumExpression" ):
                listener.enterNumExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumExpression" ):
                listener.exitNumExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumExpression" ):
                return visitor.visitNumExpression(self)
            else:
                return visitor.visitChildren(self)



    def numExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AingalLangParser.NumExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_numExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AingalLangParser.NumExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_numExpression)
                    self.state = 349
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 350
                    _la = self._input.LA(1)
                    if not(_la==22 or _la==23):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 351
                    self.term(0) 
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(AingalLangParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(AingalLangParser.TermContext,0)


        def MULTIPLY(self):
            return self.getToken(AingalLangParser.MULTIPLY, 0)

        def DIVIDED_BY(self):
            return self.getToken(AingalLangParser.DIVIDED_BY, 0)

        def MODULO(self):
            return self.getToken(AingalLangParser.MODULO, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AingalLangParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AingalLangParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 360
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 361
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 362
                    self.factor() 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AingalLangParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CastExpressionContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(AingalLangParser.LPAREN, 0)
        def typeAnnotation(self):
            return self.getTypedRuleContext(AingalLangParser.TypeAnnotationContext,0)

        def RPAREN(self):
            return self.getToken(AingalLangParser.RPAREN, 0)
        def factor(self):
            return self.getTypedRuleContext(AingalLangParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastExpression" ):
                listener.enterCastExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastExpression" ):
                listener.exitCastExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExpression" ):
                return visitor.visitCastExpression(self)
            else:
                return visitor.visitChildren(self)


    class FactorOperationContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operation(self):
            return self.getTypedRuleContext(AingalLangParser.OperationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorOperation" ):
                listener.enterFactorOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorOperation" ):
                listener.exitFactorOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorOperation" ):
                return visitor.visitFactorOperation(self)
            else:
                return visitor.visitChildren(self)


    class UnaryPlusContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(AingalLangParser.PLUS, 0)
        def factor(self):
            return self.getTypedRuleContext(AingalLangParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPlus" ):
                listener.enterUnaryPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPlus" ):
                listener.exitUnaryPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryPlus" ):
                return visitor.visitUnaryPlus(self)
            else:
                return visitor.visitChildren(self)


    class FactorIdentifierContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorIdentifier" ):
                listener.enterFactorIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorIdentifier" ):
                listener.exitFactorIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorIdentifier" ):
                return visitor.visitFactorIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class FactorFunctionCallContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(AingalLangParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorFunctionCall" ):
                listener.enterFactorFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorFunctionCall" ):
                listener.exitFactorFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorFunctionCall" ):
                return visitor.visitFactorFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class FactorNumberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(AingalLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorNumber" ):
                listener.enterFactorNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorNumber" ):
                listener.exitFactorNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorNumber" ):
                return visitor.visitFactorNumber(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(AingalLangParser.MINUS, 0)
        def factor(self):
            return self.getTypedRuleContext(AingalLangParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class FactorParensContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(AingalLangParser.LPAREN, 0)
        def numExpression(self):
            return self.getTypedRuleContext(AingalLangParser.NumExpressionContext,0)

        def RPAREN(self):
            return self.getToken(AingalLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorParens" ):
                listener.enterFactorParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorParens" ):
                listener.exitFactorParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorParens" ):
                return visitor.visitFactorParens(self)
            else:
                return visitor.visitChildren(self)


    class FactorscopedIdentifierContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def scopedIdentifier(self):
            return self.getTypedRuleContext(AingalLangParser.ScopedIdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorscopedIdentifier" ):
                listener.enterFactorscopedIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorscopedIdentifier" ):
                listener.exitFactorscopedIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorscopedIdentifier" ):
                return visitor.visitFactorscopedIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class FactorStringContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(AingalLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorString" ):
                listener.enterFactorString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorString" ):
                listener.exitFactorString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorString" ):
                return visitor.visitFactorString(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = AingalLangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_factor)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                localctx = AingalLangParser.UnaryPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.match(AingalLangParser.PLUS)
                self.state = 369
                self.factor()
                pass

            elif la_ == 2:
                localctx = AingalLangParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(AingalLangParser.MINUS)
                self.state = 371
                self.factor()
                pass

            elif la_ == 3:
                localctx = AingalLangParser.FactorFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 372
                self.functionCall()
                pass

            elif la_ == 4:
                localctx = AingalLangParser.FactorNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 373
                self.match(AingalLangParser.NUMBER)
                pass

            elif la_ == 5:
                localctx = AingalLangParser.FactorscopedIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 374
                self.scopedIdentifier()
                pass

            elif la_ == 6:
                localctx = AingalLangParser.FactorIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 375
                self.match(AingalLangParser.IDENTIFIER)
                pass

            elif la_ == 7:
                localctx = AingalLangParser.FactorStringContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 376
                self.match(AingalLangParser.STRING)
                pass

            elif la_ == 8:
                localctx = AingalLangParser.FactorOperationContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 377
                self.operation()
                pass

            elif la_ == 9:
                localctx = AingalLangParser.FactorParensContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 378
                self.match(AingalLangParser.LPAREN)
                self.state = 379
                self.numExpression(0)
                self.state = 380
                self.match(AingalLangParser.RPAREN)
                pass

            elif la_ == 10:
                localctx = AingalLangParser.CastExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 382
                self.match(AingalLangParser.LPAREN)
                self.state = 383
                self.typeAnnotation()
                self.state = 384
                self.match(AingalLangParser.RPAREN)
                self.state = 385
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def INCREMENT(self):
            return self.getToken(AingalLangParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(AingalLangParser.DECREMENT, 0)

        def SEMICOLON(self):
            return self.getToken(AingalLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = AingalLangParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(AingalLangParser.IDENTIFIER)
            self.state = 390
            _la = self._input.LA(1)
            if not(_la==34 or _la==35):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 391
                self.match(AingalLangParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReassignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(AingalLangParser.SEMICOLON, 0)

        def scopedIdentifier(self):
            return self.getTypedRuleContext(AingalLangParser.ScopedIdentifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def SUBTRACT_FROM(self):
            return self.getToken(AingalLangParser.SUBTRACT_FROM, 0)

        def numExpression(self):
            return self.getTypedRuleContext(AingalLangParser.NumExpressionContext,0)


        def DIVIDE_FROM(self):
            return self.getToken(AingalLangParser.DIVIDE_FROM, 0)

        def TIMES(self):
            return self.getToken(AingalLangParser.TIMES, 0)

        def ADD_TO(self):
            return self.getToken(AingalLangParser.ADD_TO, 0)

        def STRING(self):
            return self.getToken(AingalLangParser.STRING, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_reassignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReassignment" ):
                listener.enterReassignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReassignment" ):
                listener.exitReassignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReassignment" ):
                return visitor.visitReassignment(self)
            else:
                return visitor.visitChildren(self)




    def reassignment(self):

        localctx = AingalLangParser.ReassignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_reassignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 394
                self.scopedIdentifier()
                pass
            elif token in [68]:
                self.state = 395
                self.match(AingalLangParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.state = 402
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 398
                    self.match(AingalLangParser.ADD_TO)
                    self.state = 399
                    self.match(AingalLangParser.STRING)
                    pass

                elif la_ == 2:
                    self.state = 400
                    self.match(AingalLangParser.ADD_TO)
                    self.state = 401
                    self.numExpression(0)
                    pass


                pass
            elif token in [33]:
                self.state = 404
                self.match(AingalLangParser.SUBTRACT_FROM)
                self.state = 405
                self.numExpression(0)
                pass
            elif token in [37]:
                self.state = 406
                self.match(AingalLangParser.DIVIDE_FROM)
                self.state = 407
                self.numExpression(0)
                pass
            elif token in [36]:
                self.state = 408
                self.match(AingalLangParser.TIMES)
                self.state = 409
                self.numExpression(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 412
            self.match(AingalLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolOrExpression(self):
            return self.getTypedRuleContext(AingalLangParser.BoolOrExpressionContext,0)


        def getRuleIndex(self):
            return AingalLangParser.RULE_boolExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpression" ):
                listener.enterBoolExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpression" ):
                listener.exitBoolExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpression" ):
                return visitor.visitBoolExpression(self)
            else:
                return visitor.visitChildren(self)




    def boolExpression(self):

        localctx = AingalLangParser.BoolExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_boolExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.boolOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AingalLangParser.RULE_boolOrExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LogicOrContext(BoolOrExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolOrExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.BoolAndExpressionContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.BoolAndExpressionContext,i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.OR)
            else:
                return self.getToken(AingalLangParser.OR, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOr" ):
                listener.enterLogicOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOr" ):
                listener.exitLogicOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOr" ):
                return visitor.visitLogicOr(self)
            else:
                return visitor.visitChildren(self)



    def boolOrExpression(self):

        localctx = AingalLangParser.BoolOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_boolOrExpression)
        self._la = 0 # Token type
        try:
            localctx = AingalLangParser.LogicOrContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.boolAndExpression()
            self.state = 421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 417
                self.match(AingalLangParser.OR)
                self.state = 418
                self.boolAndExpression()
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AingalLangParser.RULE_boolAndExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LogicAndContext(BoolAndExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolAndExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolNotExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.BoolNotExpressionContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.BoolNotExpressionContext,i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(AingalLangParser.AND)
            else:
                return self.getToken(AingalLangParser.AND, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicAnd" ):
                listener.enterLogicAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicAnd" ):
                listener.exitLogicAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAnd" ):
                return visitor.visitLogicAnd(self)
            else:
                return visitor.visitChildren(self)



    def boolAndExpression(self):

        localctx = AingalLangParser.BoolAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_boolAndExpression)
        self._la = 0 # Token type
        try:
            localctx = AingalLangParser.LogicAndContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.boolNotExpression()
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 425
                self.match(AingalLangParser.AND)
                self.state = 426
                self.boolNotExpression()
                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolNotExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AingalLangParser.RULE_boolNotExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LogicPrimaryWrapContext(BoolNotExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolNotExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolPrimary(self):
            return self.getTypedRuleContext(AingalLangParser.BoolPrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicPrimaryWrap" ):
                listener.enterLogicPrimaryWrap(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicPrimaryWrap" ):
                listener.exitLogicPrimaryWrap(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicPrimaryWrap" ):
                return visitor.visitLogicPrimaryWrap(self)
            else:
                return visitor.visitChildren(self)


    class LogicNotContext(BoolNotExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolNotExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(AingalLangParser.NOT, 0)
        def boolNotExpression(self):
            return self.getTypedRuleContext(AingalLangParser.BoolNotExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicNot" ):
                listener.enterLogicNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicNot" ):
                listener.exitLogicNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicNot" ):
                return visitor.visitLogicNot(self)
            else:
                return visitor.visitChildren(self)



    def boolNotExpression(self):

        localctx = AingalLangParser.BoolNotExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_boolNotExpression)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                localctx = AingalLangParser.LogicNotContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(AingalLangParser.NOT)
                self.state = 433
                self.boolNotExpression()
                pass
            elif token in [6, 18, 20, 22, 23, 47, 51, 53, 54, 61, 62, 68]:
                localctx = AingalLangParser.LogicPrimaryWrapContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.boolPrimary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolPrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AingalLangParser.RULE_boolPrimary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringComparisonContext(BoolPrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolPrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stringExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.StringExpressionContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.StringExpressionContext,i)

        def EQUALS(self):
            return self.getToken(AingalLangParser.EQUALS, 0)
        def NOT_EQUALS(self):
            return self.getToken(AingalLangParser.NOT_EQUALS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringComparison" ):
                listener.enterStringComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringComparison" ):
                listener.exitStringComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringComparison" ):
                return visitor.visitStringComparison(self)
            else:
                return visitor.visitChildren(self)


    class FalseLiteralContext(BoolPrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolPrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE_VALUE(self):
            return self.getToken(AingalLangParser.FALSE_VALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseLiteral" ):
                listener.enterFalseLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseLiteral" ):
                listener.exitFalseLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseLiteral" ):
                return visitor.visitFalseLiteral(self)
            else:
                return visitor.visitChildren(self)


    class NumComparisonContext(BoolPrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolPrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def numExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.NumExpressionContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.NumExpressionContext,i)

        def comparisonOp(self):
            return self.getTypedRuleContext(AingalLangParser.ComparisonOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumComparison" ):
                listener.enterNumComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumComparison" ):
                listener.exitNumComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumComparison" ):
                return visitor.visitNumComparison(self)
            else:
                return visitor.visitChildren(self)


    class LogicParenContext(BoolPrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolPrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(AingalLangParser.LPAREN, 0)
        def boolExpression(self):
            return self.getTypedRuleContext(AingalLangParser.BoolExpressionContext,0)

        def RPAREN(self):
            return self.getToken(AingalLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicParen" ):
                listener.enterLogicParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicParen" ):
                listener.exitLogicParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicParen" ):
                return visitor.visitLogicParen(self)
            else:
                return visitor.visitChildren(self)


    class TrueLiteralContext(BoolPrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolPrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE_VALUE(self):
            return self.getToken(AingalLangParser.TRUE_VALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueLiteral" ):
                listener.enterTrueLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueLiteral" ):
                listener.exitTrueLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueLiteral" ):
                return visitor.visitTrueLiteral(self)
            else:
                return visitor.visitChildren(self)


    class LogicIdentifierContext(BoolPrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolPrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(AingalLangParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicIdentifier" ):
                listener.enterLogicIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicIdentifier" ):
                listener.exitLogicIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicIdentifier" ):
                return visitor.visitLogicIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class MatrixComparisonContext(BoolPrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AingalLangParser.BoolPrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matrixExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AingalLangParser.MatrixExpressionContext)
            else:
                return self.getTypedRuleContext(AingalLangParser.MatrixExpressionContext,i)

        def EQUALS(self):
            return self.getToken(AingalLangParser.EQUALS, 0)
        def NOT_EQUALS(self):
            return self.getToken(AingalLangParser.NOT_EQUALS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixComparison" ):
                listener.enterMatrixComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixComparison" ):
                listener.exitMatrixComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixComparison" ):
                return visitor.visitMatrixComparison(self)
            else:
                return visitor.visitChildren(self)



    def boolPrimary(self):

        localctx = AingalLangParser.BoolPrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_boolPrimary)
        self._la = 0 # Token type
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = AingalLangParser.NumComparisonContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.numExpression(0)
                self.state = 438
                self.comparisonOp()
                self.state = 439
                self.numExpression(0)
                pass

            elif la_ == 2:
                localctx = AingalLangParser.StringComparisonContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.stringExpression()
                self.state = 442
                _la = self._input.LA(1)
                if not(_la==27 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 443
                self.stringExpression()
                pass

            elif la_ == 3:
                localctx = AingalLangParser.MatrixComparisonContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.matrixExpression()
                self.state = 446
                _la = self._input.LA(1)
                if not(_la==27 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 447
                self.matrixExpression()
                pass

            elif la_ == 4:
                localctx = AingalLangParser.LogicParenContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 449
                self.match(AingalLangParser.LPAREN)
                self.state = 450
                self.boolExpression()
                self.state = 451
                self.match(AingalLangParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = AingalLangParser.TrueLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 453
                self.match(AingalLangParser.TRUE_VALUE)
                pass

            elif la_ == 6:
                localctx = AingalLangParser.FalseLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 454
                self.match(AingalLangParser.FALSE_VALUE)
                pass

            elif la_ == 7:
                localctx = AingalLangParser.LogicIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 455
                self.match(AingalLangParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(AingalLangParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(AingalLangParser.NOT_EQUALS, 0)

        def GREATER_THAN(self):
            return self.getToken(AingalLangParser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(AingalLangParser.LESS_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(AingalLangParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(AingalLangParser.LESS_EQUAL, 0)

        def getRuleIndex(self):
            return AingalLangParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOp" ):
                return visitor.visitComparisonOp(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOp(self):

        localctx = AingalLangParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 279038656512) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.numExpression_sempred
        self._predicates[30] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def numExpression_sempred(self, localctx:NumExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




