from __future__ import unicode_literals, print_function
from Grammar import *
import sys
"""
/*****************************************************
Module Description: Here we will save the parser output in an output file
/*****************************************************
"""

#This will contain the source code of the user in 1 single string 
outpath = "source.txt"
parsestring = ''
inpath = raw_input("Enter izitag source file path:  ")

with open(inpath, 'r') as content_file:
	content = content_file.read()
	#f is the parser
	parsestring = content
	content_file.close()

f = parse(parsestring, IziTag)

with open(outpath, 'w+') as source_write:
	source_write.write(content)
	source_write.close() 


"""
#Write Output to a text file to be interpreted for the intermidiate code 
with open("out.txt", "wt") as out_file:
    for e in f.block:
        out_file.write(e +'\n')
 """

