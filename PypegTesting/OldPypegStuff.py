import re, fileinput
import pyPEG
from pyPEG import parse
from pyPEG import keyword, _and, _not, ignore

# pyPEG:
#
#   basestring:     terminal symbol (characters)
#   keyword:        terminal symbol (keyword)
#   matchobj:       terminal symbols (regex, use for scanning symbols)
#   function:       named non-terminal symbol, recursive definition
#                   if you don't want naming in output, precede name with an underscore
#   tuple:          production sequence
#   integer:        count in production sequence:
#                    0: following element is optional
#                   -1: following element can be omitted or repeated endless
#                   -2: following element is required and can be repeated endless
#   list:           options, choose one of them
#   _not:           next element in production sequence is matched only if this would not
#   _and:           next element in production sequence is matched only if this would, too

# comment <- r"//.*" | r"/\*.**?\*/";

"""
Language to replicate:

function fak(n) {
    if (n==0) { // 0! is 1 by definition
        return 1;
    } else {
        return n * fak(n - 1);
    };
}
"""




def comment():          return [re.compile(r"//.*"), re.compile("/\*.*?\*/", re.S)]

# literal <- r'\d*\.\d*|\d+|".*?"';
def literal():          return re.compile(r'\d*\.\d*|\d+|".*?"')

# symbol <- r"\w+"
def symbol():           return re.compile(r"\w+")

# operator <- r"\+|\-|\*|\/|\=\=";
def operator():         return re.compile(r"\+|\-|\*|\/|\=\=")

# operation <- symbol operator (literal | functioncall);
def operation():        return symbol, operator, [literal, functioncall]

# expression <- literal | operation | functioncall;
def expression():       return [literal, operation, functioncall]

# expressionlist <- expression ("," expression)*;
def expressionlist():   return expression, -1, (",", expression)

# returnstatement <- k"return" expression;
def returnstatement():  return keyword("return"), expression

# ifstatement <- k"if" "(" expression ")" block k"else" block;
def ifstatement():      return keyword("if"), "(", expression, ")", block, keyword("else"), block

# statement <- (ifstatement | returnstatement) ";";
def statement():        return [ifstatement, returnstatement], ";"

# block <- "{" statement+ "}";
def block():            return "{", -2, statement, "}"

# parameterlist <- "(" symbol ("," symbol)* ")";
def parameterlist():    return "(", symbol, -1, (",", symbol), ")"

# functioncall <- symbol "(" expressionlist ")";
def functioncall():     return symbol, "(", expressionlist, ")"

# function <- k"function" symbol parameterlist block;
def function():         return keyword("function"), symbol, parameterlist, block

# simpleLanguage <- function;
def simpleLanguage():   return function

pyPEG.print_trace = True

files = fileinput.input()
result = parse(simpleLanguage(), files, True, comment)
print result
