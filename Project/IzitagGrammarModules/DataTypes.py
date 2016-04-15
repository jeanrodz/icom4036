from __future__ import unicode_literals, print_function
from pypeg2 import *

"""
/*****************************************************
Module Description: Here we define how a datatype looks like in izitag
/*****************************************************
"""

class StringLiteral(str):
     #fulltString = "'", maybe_some(word),"'"
     emptyString = "''"
     fullString = re.compile(r'(.*\S.*)')
     grammar = [emptyString,fullString]
     
class IntLiteral(str):
     grammar = re.compile(r"\d+")
     
class FloatLiteral(str):
    grammar= re.compile(r'(\d+(.\d+)?)')
    
class ArrayLiteral(str):
    grammar = re.compile("(\[.*\])")
    
class StringDataType(Keyword):
    grammar = Enum(  K("string"))

class StringType(str):
    grammar = StringDataType
    
class IntDataType(Keyword):
    grammar = Enum( K("int"))
    
class IntType(str):
    grammar = IntDataType

class FloatDataType(Keyword):
    grammar = Enum(  K("float"))
    
class FloatType(str):
    grammar = FloatDataType
    
class ArrayDataType(Keyword):
    grammar = Enum( K("array"))
    
class ArrayType(str):
    grammar = ArrayDataType
    
class DataType(Keyword):
    grammar = Enum( K("int"), K("float") , K("string"),K("array"))
    
class Type(str):
    grammar = DataType
    


    
"""
stringToParse = " 99 "
f = parse(stringToParse, IntLiteral)
print(f)

stringToParse = "1.0"
f = parse(stringToParse, FloatLiteral)
print(f)

stringToParse = " 'ThisIsASingleString' "
f = parse(stringToParse, StringLiteral)
print(f)


stringToParse = " int  "
f = parse(stringToParse, DataType)
print(f)

stringToParse = " float  "
f = parse(stringToParse, DataType)
print(f)


stringToParse = " int  "
f = parse(stringToParse, IntDataType)
print(f)
    
stringToParse = " String  "
f = parse(stringToParse, DataType)
print(f)
"""