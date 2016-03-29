from __future__ import unicode_literals, print_function
from pypeg2 import *
from DataTypes import *
from Identifier import *
from Assignment import *
from Parameter import *

"""
/*****************************************************
Module Description: Here we define how a function looks like in izitag
/*****************************************************
"""

class Function(str):
    grammar = attr("functionName",Identifier),"(",attr("functionParameters",Parameters),")",";"
string = "iziTag( foo,5);"

f = parse(string,Function)

print(f.functionName)
print(f.functionParameters)


