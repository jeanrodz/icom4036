from __future__ import unicode_literals, print_function
from pypeg2 import *
from DataTypes import *
from Identifier import *
from Function import *
"""
/*****************************************************
Module Description: Here we define how an assignment looks like in izitag
/*****************************************************
"""


class Expression(str):
    grammar = [FloatLiteral,IntLiteral,StringLiteral]
    
class ArrayExpression(str):
    grammar = ArrayType, Identifier, ":=", ArrayLiteral, ";"
    
class IntExpression(str):
    grammar = IntType, Identifier, ":=",IntLiteral,";"
    
class FloatExpression(str):
    grammar = FloatType, Identifier, ":=",FloatLiteral,";"
    
class StringExpression(str):
    grammar = StringType, Identifier, ":=", StringLiteral

class Assignment(str):
    grammar = [ArrayExpression,IntExpression,FloatExpression,StringExpression]
  
string = "array blah := ['hi', 'balhs'];"
f = parse(string, ArrayExpression)
print(f)
