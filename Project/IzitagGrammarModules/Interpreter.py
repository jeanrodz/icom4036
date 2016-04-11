from __future__ import unicode_literals, print_function
from yattag import Doc


"""
/*****************************************************
Module Description: Here we will use the dictionaries for the state machine :)
/*****************************************************
"""

stateDictionary = {(1, 'int'): 2,
                   (1, 'iziPar'): 10, }

def MainMachine(file,currentState,stateDictionary,maxStates):
    
    with open(file,"rt") as in_file:
        for line in in_file:
            newline = line.replace("\n","")
            print(newline)
            nl = newline.replace("[","")
            nl = nl.replace("]","")
            nl = nl.replace("'","")
            nl = nl.split(", ")
            print(nl[0])
            
            
    
print(MainMachine("source.txt", 1, stateDictionary, 11))







