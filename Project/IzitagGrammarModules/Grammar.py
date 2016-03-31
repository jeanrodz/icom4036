
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
    
string = "iziTag {  /* My First IziTag Program*/   String text := 'testing' ; iziTitle(text);  int parId_1 := 1; String parText := 'hello'; iziPar(parId_1, parText); }"

f = parse(string, IziTag)

print(f.block)


"""
print(len(f.block))
print(f.block[0])
print(f.block[1])
"""