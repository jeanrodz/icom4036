from __future__ import unicode_literals, print_function
from pypeg2 import *

"""
/*****************************************************
Module Description: 
Defined Grammar Syntax of the IziTag Language
/*****************************************************
"""


"""
Here we have the list of reserved keywords for izitag
"""
class ReservedKeywords(Keyword):
    grammar = Enum( K("return") )
    
"""Reserved Keywords of iziTag so far """
class DataType(Keyword):
    grammar = Enum( K("int"), K("bool") , K("String"))
    

"""
The IziTag language will support the commentary of C++ style which is provided below:
Example of a comment in IziTag:

//Hello This is a comment in iziTag

"""
class Comment(str):
    grammar = comment_cpp
"""
A literal is s a notation for representing a fixed value in source code. 
Almost all programming languages have notations for atomic values such as integers, 
floating-point numbers, and strings, and usually for booleans and characters.

In this case is looking for digits
Example of a Literal in IziTag:
123
0.01
9.009
0
1
433.909
"""
class Literal(str):
    grammar= re.compile(r'(\d+(.\d+)?)')
    
class BoolLiteral(Symbol):
  grammar = Enum( K("True"), K("False") )

class StringLiteral(str):
     quoted_string = re.compile(r'"[^"]*"')
     grammar = [word, quoted_string]
     
class Int:
     grammar = re.compile(r"\d+")
    
    
    
"""
This will represent identifiers or variables that match with the following rule:
1) identifier must start with character or _ it cannot start with a symbol
example of valid identifier: __fooIsCool
example of invalid identifier: 7&fooIsCool
"""
class Identifier(str):
    grammar = re.compile(r"[^\d\W]\w*")
    

"""
This will support the basic operators which are:
+ | - | * | \ | == 

Example of a Operators in IziTag:
9 +2
3-3
2-8
4/2
2 == 2
"""
class Operator(str):
    grammar = re.compile(r"\+|\-|\*|\/|\=\=")
    
"""
An Operation consists of the following it can be 
x + factorial(5)
foo == 10
x * y
5*3
10 == 30
Falta add el function call like this 
grammar =  [ParenthesesMatch,''],[Literal,Identifier], Operator, [Literal,Identifier,FunctionCall],[ParenthesesMatch,'']

"""

class Operation(str):
    grammar =  [Literal,Identifier], Operator, [Literal,Identifier]
    
    
"""
A Single expression can be from the simplest as follow for now:

1
5 + 5
foo()
(foo())
(4+3)
(1)
Falta add the function call class so it can be like this 
grammar = [ParenthesesMatch,''],[Literal, Operation, Functioncall],[ParenthesesMatch,'']
"""
class Expression(str):
    grammar = [Literal, Operation]
    
"""
A List expression can be form 0 or many expressions which -1 represents the * cardinality (zero or more)
"""
class ExpressionList(str):
    grammar = Expression, -1, (",", Expression)
    
"""
Here we have the return statement for the izitag language:
Example:
return 5+10;
"""
class Return(str):
    grammar = "return", Expression,";"


class Assignment(str):
    grammar = attr("type", DataType), attr("identifier",Identifier ), ":=" , attr("expression", Expression) , ";"
    
    
class Parameter:
    grammar = attr("typing", DataType), attr("parameterIdentifier", Identifier)
    
class Parameters(Namespace):
    grammar = optional(csl(Parameter))
    

class Instruction(str):
    grammar = Assignment
    
block = "{", maybe_some(Instruction), "}"



stringToParse = " bool isValid,int foo "
f = parse(stringToParse,Parameters)
print(f)



     




    
    
