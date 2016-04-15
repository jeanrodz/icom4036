from __future__ import unicode_literals, print_function
from pypeg2 import *
from Function import *
from array import ArrayType


"""
/*****************************************************
Module Description: Here we define how a datatype looks like in izitag
/*****************************************************
"""
class IziTagFunctionKeywords(Keyword):
    grammar = Enum( K("iziTitle"),K("iziPar"), K("iziSection"),K("iziHeader"),K("iziTable"),K("iziImage"),K("iziList"))

class ListKeywords(Keyword):
    grammar = Enum( K("ordered"),K("unordered"))
    
class IziTagFunctionName(str):
    grammar = IziTagFunctionKeywords
    
class IziTagListOrder(str):
    grammar = ListKeywords
            
class IziTitle(str):
    grammar = IziTagFunctionName,"(",[Identifier],")"
    
class IziPar(str):
    grammar = IziTagFunctionName,"(", [Identifier], ")"

class IziSection(str):
    grammar = IziTagFunctionName,"(", Identifier,")"
    
class IziHeader(str):
    grammar = IziTagFunctionName,"(",StringLiteral,")"

class IziTable(str):
    grammar = IziTagFunctionName,"(",Identifier,",",optional(csl(Identifier)), ")"

class IziImage(str):
    grammar = IziTagFunctionName,"(",[Identifier],",", [Identifier], ",", [Identifier],")"
    
class IziList(str):
    grammar = IziTagFunctionName,"(",IziTagListOrder,",",Identifier,")"
    
class IziTagFunctions(str):
    grammar = [IziTitle,IziPar,IziSection,IziHeader,IziTable,IziImage,IziList]
    
    

    



