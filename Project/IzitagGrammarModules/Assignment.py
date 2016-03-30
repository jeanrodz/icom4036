from __future__ import unicode_literals, print_function
from pypeg2 import *
from DataTypes import *
from Identifier import *

"""
/*****************************************************
Module Description: Here we define how an assignment looks like in izitag
/*****************************************************
"""


class Expression(str):
    grammar = [FloatLiteral,IntLiteral,StringLiteral]

class Assignment(str):
    grammar =  Type,Identifier , ":=" , Expression , ";"
  
stringToParse = "float foo := 0.1 ;" 

f = parse(stringToParse, Assignment)
print(f)
