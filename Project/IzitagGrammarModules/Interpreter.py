from __future__ import unicode_literals, print_function
from yattag import Doc


"""
/*****************************************************
Module Description: Here we will use the dictionaries for the state machine :)
/*****************************************************
"""

token_stack = []

def load_tokens(file): 
    with open(file,"rt") as in_file:
        for line in in_file:
            newline = line.replace("\n","")
            nl = newline.replace("[","")
            nl = nl.replace("]","")
            nl = nl.replace("'","")
            nl = nl.split(", ")
            token_stack.append(nl)
            
load_tokens('source.txt')            
"""
Data Definitions
"""

current_token = 0
int_collection = {}
float_collection = {}
string_collection = {}
array_collection = {}

"""
Parse-Map Dictionary
"""


def data_type_assignment(current_token):
    if(token[0] == 'int'): int_collection[token[1]] = token[2]
    elif (token[0] == 'float'): float_collection[token[1]] = token[2]
    else : string_collection[token[1]] = token[2]


parse_map = {
    'int' : data_type_assignment,
    'float' : data_type_assignment,
    'string' : data_type_assignment,
    }

for token in token_stack:
    parse_map[token[0]]
    current_token = current_token + 1

print(token_stack)
print(string_collection)

