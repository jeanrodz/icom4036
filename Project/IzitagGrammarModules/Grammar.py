
from __future__ import unicode_literals, print_function
from pypeg2 import *
from Function import *
from IzitagFunctions import *



"""
/*****************************************************
Module Description: Here we define how a function looks like in izitag
/*****************************************************
"""

class Instruction(str):
    grammar = [Assignment,IziTitle]
    
class IziTag(str):
    grammar = "iziTag","{",attr("block",maybe_some(Instruction)),"}"
    
string = "iziTag{ int foo := 6; iziTitle( 'jose');  }"

f = parse(string, IziTag)

print(f)
"""
print(len(f.block))
print(f.block[0])
print(f.block[1])
"""