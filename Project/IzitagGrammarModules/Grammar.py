
from __future__ import unicode_literals, print_function
from pypeg2 import *
from Function import *


"""
/*****************************************************
Module Description: Here we define how a function looks like in izitag
/*****************************************************
"""

class Instruction(str):
    grammar = [Assignment,Function]
    
class IziTag(List):
    grammar = "iziTag","{",attr("block",maybe_some(Instruction)),"}"
    
string = "iziTag{ int foo := 6; zTitle( a, 9 , 0.8 , '');  }"

f = parse(string, IziTag)

print(len(f.block))
print(f.block[0])
print(f.block[1])