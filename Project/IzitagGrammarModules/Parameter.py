from __future__ import unicode_literals, print_function
from pypeg2 import *
from DataTypes import *
from Identifier import *
from Assignment import *


"""
/*****************************************************
Module Description: Here we define how a parameter looks like in izitag
/*****************************************************
"""


""""
NOTE HAY CONFLICT EN RECONOCER UN IDENTIFIER Y UN STRING COMO EXPRESSION
"""
class Parameter:
    grammar = [attr("paramIdentifier", Identifier), attr("paramExpression", Expression)]
    
class Parameters(Namespace):
    grammar = optional(csl(Parameter))
    
strings = " 'jose' "

f = parse(strings,Parameter)
print(f.paramExpression)


    
