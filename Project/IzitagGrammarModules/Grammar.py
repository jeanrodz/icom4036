
from __future__ import unicode_literals, print_function
from pypeg2 import *
from Function import *
from Comment import *
from IzitagFunctions import *



"""
/*****************************************************
Module Description: Here we define how a function looks like in izitag
/*****************************************************
"""

class Instruction(str):
    grammar = [Assignment,IziTagFunctions,Comment], endl
    
class IziTag(str):
    grammar = "iziTag","{",attr("block",maybe_some(Instruction)),"}"
    



"""
print(len(f.block))
print(f.block[0])
print(f.block[1])
"""