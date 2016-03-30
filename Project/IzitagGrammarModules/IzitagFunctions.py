from __future__ import unicode_literals, print_function
from pypeg2 import *
from Function import *


"""
/*****************************************************
Module Description: Here we define how a datatype looks like in izitag
/*****************************************************
"""
class IziTagFunctionKeywords(Keyword):
    grammar = Enum( K("iziTitle"))
    
class IziTagFunctionName(str):
    grammar = IziTagFunctionKeywords
    
class TextParameter(str):
    grammar =  optional(StringLiteral)
    
class IziTitle(str):
    grammar = IziTagFunctionName,"(",TextParameter,")",";"

string = "iziTitle('jose');"

f = parse(string,IziTitle)
print(f)