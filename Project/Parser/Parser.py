from __future__ import unicode_literals, print_function
from pypeg2 import *
"""
In this module we have the paring of a regular function C style like this

    type functionName(type name, type name ...)
    { //Comment for this block of code
      instructions
    }
An example is as followed

 int functionName( int a, long b)
 {
     do_this;
     do_that;
 }

"""
""" With pyPeg you declare a Python class for each object you want to parse
This class is then instantiated for each parsed object. This class gets an attribute with a 
description of what should be parsed. 
"""
#-----------------------------------------------------------------------------------------------
"""
A Type is a reserved keyword such as an int, short, long ,boolean
If its  a Type we should pass the class Keywords in which it works with the Enum

Keyword(Symbol)

Used to access the keyword table.
The Keyword class is meant to be instanciated for each Keyword of the source language. 
The class holds the keyword table as a Namespace instance. 
There is the abbreviation K for Keyword. The latter is useful for instancing keywords. 

"""
class Type(Keyword):
    grammar = Enum( K("int"), K("short") , K("long"), K("boolean") )
      
class Parameter:
    grammar = attr("typing", Type), name() 

class Parameters(Namespace):
    grammar = optional(csl(Parameter))
    
class Instruction(str):
    grammar = word, ";"
    
block = "{", maybe_some(Instruction), "}"
    
class Function(List):
    grammar = attr("typing", Type), name(), \
    "(", attr("parms", Parameters), ")", block
    
stringToParse = "int functionName(int a, long b) { do_this; do_that; }"
f = parse(stringToParse, Function)

print(f.name)

if f.name == "functionName":
    print("YAY We got out first function name parsed !!")


print(f.parms["a"].typing)
print(f.parms["b"].typing)
print(f[0])
print(f[1])


