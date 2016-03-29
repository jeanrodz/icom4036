from __future__ import unicode_literals, print_function
from pypeg2 import *

"""
/*****************************************************
Module Description: Here we define how a identifier looks like
/*****************************************************
"""


"""
This will represent identifiers or variables that match with the following rule:
1) identifier must start with character or _ it cannot start with a symbol
example of valid identifier: __fooIsCool
example of invalid identifier: 7&fooIsCool
"""
class Identifier(str):
    grammar = re.compile(r"[^\d\W]\w*")
    

stringToParse = " __Foo_is_A_Cool_Identifier__lol_ "
f = parse(stringToParse, Identifier)
print(f)