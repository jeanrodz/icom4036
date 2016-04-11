from __future__ import unicode_literals, print_function
from ParseOutputGen import *

"""
/*****************************************************
Module Description: Here we will use the dictionaries for the state machine
/*****************************************************
"""

stateDictionary = {(1, 'int'): 2,
                   (1, 'iziPar'): 10, }

def MainMachine(file,currentState,stateDictionary,maxStates):
    
    with open(file,"rt") as in_file:
        for line in in_file:
            newline = line.replace("\n","")
            print(newline)
            nl = newline
            nl.partition('[')[1].rpartition(']')[1]
            print(nl)
    
print(MainMachine("out.txt", 1, stateDictionary, 11))

"""
s = "[virus 1 [isolated from china]]"
s.partition('[')[-1].rpartition(']')[0]
'virus 1 [isolated from china]'
"""