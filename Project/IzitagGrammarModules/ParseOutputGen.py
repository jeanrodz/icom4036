from __future__ import unicode_literals, print_function
from Grammar import *
import sys
"""
/*****************************************************
Module Description: Here we will save the parser output in an output file
/*****************************************************
"""

#This will contain the source code of the user in 1 single string 
mySource = "iziTag{  int foo :=5;  iziPar(foo,'hola');  }"

#f is the parser
f = parse(mySource, IziTag)

#Write Output to a text file to be interpreted for the intermidiate code 
with open("out.txt", "wt") as out_file:
    for e in f.block:
        out_file.write(e +'\n')
    
    



