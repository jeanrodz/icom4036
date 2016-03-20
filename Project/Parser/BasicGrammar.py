from __future__ import unicode_literals, print_function
from pypeg2 import *
"""
Parsing

A str instance as well as an instance of pypeg2.
Literal is parsed in the source text as a Terminal Symbol. 
It is removed and no result is put into the Abstract syntax tree. 
If it does not exist at the correct position in the source text, a SyntaxError is raised. 

"""
class Key(str):
    grammar = name(), "=" , restline, endl

string = "thisVariableMustBeSureIsCorrectNotAllowingToHaveErros = something here to do"
parsedKey = parse(string,Key)
print(parsedKey.name)
print(parsedKey)

"""
Composing statements  using compose
"""
#This will put the string "a value" after the = 
k = Key("a value") #Seting the string  
k.name = Symbol("give me") #Set name() symbol as give me   
print("The name symbol is " + k.name)  
print("The rest of line expression after = is "+k)     
print("Full compositions is " +compose(k)) # return the full expression as give me= a value

"""
list instantiation:

they represent different options tied toegther, each one is tested until a valid match
is found. If none matches we get syntax error

"""

numberRegex = re.compile(r"\d+")
print(parse("hello", [numberRegex, word]))

letters = re.compile(r"[a-zA-Z]") 
number = re.compile(r"\d+")
print(compose(23, [letters, number]))

"""

Class Symbol
Class definition

Symbol(str)

Used to scan a Symbol.

If you're putting a Symbol somewhere in your grammar,
 then Symbol.regex is used to scan while parsing. 
 The result will be a Symbol instance. 
 Optionally it is possible to check that a Symbol instance will not be identical to any Keyword instance. 
 This can be helpful if the source language forbids that.

A class which is derived from Symbol can have an Enum as its grammar only. Other values for its grammar are forbidden and will raise a TypeError. If such an Enum is specified, each parsed value will be checked if being a member of this Enum additionally to the RegEx matching. 
"""

#This is used to scan while parsing only for symbols followed by a whitespace
Symbol.regex = re.compile(r"[\w\s]+")
class Symbols(str):
    grammar = name(), "=", restline, endl

k = parse("this one=foo bar", Key)
print(k.name)
print(Symbol('this one'))

"""
Keyword(Symbol)

Used to access the keyword table.

The Keyword class is meant to be instanciated for each Keyword of the source language. 
The class holds the keyword table as a Namespace instance. 
There is the abbreviation K for Keyword. The latter is useful for instancing keywords. 
"""

class Type(Keyword):
     grammar = Enum( K("int"), K("long") )
kType = parse("int", Type)
print(kType)








