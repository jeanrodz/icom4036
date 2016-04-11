from __future__ import unicode_literals, print_function
from pypeg2 import *
from Function import *


"""
/*****************************************************
Module Description: Here we define how a datatype looks like in izitag
/*****************************************************
"""
class IziTagFunctionKeywords(Keyword):
    grammar = Enum( K("iziTitle"),K("iziPar"), K("iziSection"),K("iziHeader"),K("iziTable"),K("iziImage"),K("iziList"))

class ListKeywords(Keyword):
    grammar = Enum(K("ordered"),K("unordered"))
    
class IziTagFunctionName(str):
    grammar = IziTagFunctionKeywords
    
class IziTagListOrder(str):
    grammar = ListKeywords
            
class IziTitle(str):
    grammar = IziTagFunctionName,"(",[Identifier,StringLiteral],")",";"
    
class IziPar(str):
    grammar = IziTagFunctionName,"(",[Identifier,IntLiteral],",",[StringLiteral,Identifier], ")",";"

class IziSection(str):
    grammar = IziTagFunctionName,"(",")",";"
    
class IziHeader(str):
    grammar = IziTagFunctionName,"(",StringLiteral,")",";"

class IziTable(str):
    grammar = IziTagFunctionName,"(",IntLiteral,",",IntLiteral,"," , IntLiteral , ")",";"

class IziImage(str):
    grammar = IziTagFunctionName,"(",IntLiteral,",",StringLiteral,")",";"
    
class IziList(str):
    grammar = IziTagFunctionName,"(",IntLiteral,",",IziTagListOrder,",",Identifier,")",";"
    
class IziTagFunctions(str):
    grammar =[IziTitle,IziPar,IziSection,IziHeader,IziTable,IziImage,IziList]
    


    



