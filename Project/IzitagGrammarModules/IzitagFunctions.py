from __future__ import unicode_literals, print_function
from pypeg2 import *
from Function import *


"""
/*****************************************************
Module Description: Here we define how a datatype looks like in izitag
/*****************************************************
"""
class IziTagFunctionKeywords(Keyword):
    grammar = Enum( K("iziTitle"),K("iziPar"), K("iziSection"),K("iziHeader"),K("iziTable"),K("iziImage"))
    
class IziTagFunctionName(str):
    grammar = IziTagFunctionKeywords
            
class IziTitle(str):
    grammar = IziTagFunctionName,"(",[Identifier,StringLiteral],")",";"

class IziSection(str):
    grammar = IziTagFunctionName,"(",")",";"
    
class IziHeader(str):
    grammar = IziTagFunctionName,"(",StringLiteral,")",";"

class IziTable(str):
    grammar = IziTagFunctionName,"(",IntLiteral,",",IntLiteral,"," , IntLiteral , ")",";"

class IziImage(str):
    grammar = IziTagFunctionName,"(",IntLiteral,",",StringLiteral,")",";"
    
string = "iziImage(5,'foo');"

f = parse(string,IziImage)

    



