from __future__ import unicode_literals, print_function
from pypeg2 import *

"""
/*****************************************************
Module Description: Here we define how a comment is defined in izitag by using c++ comment style
/*****************************************************
"""


"""
The IziTag language will support the commentary of C++ style which is provided below:
Example of a comment in IziTag:

//Hello This is a comment in iziTag

"""
class Comment(str):
    grammar = comment_cpp

stringToParse = " // Hello this is a comment in iziTag "
f = parse(stringToParse, Comment)
print(f)