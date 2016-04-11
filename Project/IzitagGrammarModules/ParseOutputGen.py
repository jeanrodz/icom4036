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
inpath = input("Enter izitag source file path:  ")

try:
	with open(inpath, 'r') as content_file:
		content = content_file.read()
		parsestring = content
		content_file.close()
	parsestring.replace("str: ", "")
	print(parsestring)
except:
	raise Exception("File not found or does not exist")

f = parse(parsestring, IziTag)
print(f.block)
with open(outpath, 'w+') as source_write:
	 for e in f.block: 
	 	source_write.write(e +'\n')
	 source_write.close()
 



