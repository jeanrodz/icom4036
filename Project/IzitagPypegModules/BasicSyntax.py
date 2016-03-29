from __future__ import unicode_literals, print_function
from pypeg2 import *

"""
This modules works on assigning a value to a variable

An assignment has the following characteristics:

Defining what an assignment statement can be in EBNF:

<assignStatement> := <datatype> <identifier> ':=' <expression>';'
"""

"""
The IziTag language will support the commentary of C++ style which is provided below:
// This is a comment
"""
class Comment(str):
    grammar = comment_cpp

"""
A literal is s a notation for representing a fixed value in source code. 
Almost all programming languages have notations for atomic values such as integers, 
floating-point numbers, and strings, and usually for booleans and characters.

In this case is looking for digits 
"""

class Literal(str):
    grammar= re.compile(r'\d*\.\d*|\d+|".*?"')
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
+ | - | * | \ | = | #t | #f | #or | #and | #not
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
    
""""
NOTE!!!!!!!1
Remains to add a list of Expression 
"""


"""Reserved Keywords of iziTag so far """
class DataType(Keyword):
    grammar = Enum( K("int"), K("bool") , K("String"))
    
class ReservedKeywords:
    grammar = Enum(  K("if"),K("else"),K("return"),K("true"),K("false"),K("izitag") )
    
""" An assignment in izitag conforms with the following rule:
     <datatype> <identifier> := <expression>;
"""
class Assignment(str):
    grammar = attr("type", DataType), attr("identifier",Identifier ), ":=" , attr("expression", Expression) , ";"
    

stringToParse = " int foo   :=   5 ;"
f = parse(stringToParse,Assignment)
print(f.type)
print(f.identifier)
print(f.expression)











"""


class Type(Keyword):
    grammar = Enum( K("int"), K("bool") , K("String") )

    
class String(str):
    grammar = re.compile(r"\"[^\"]+\"")

class BoolLiteral(Symbol):
     grammar = Enum( K("True"), K("False") )
     
class Digit(str):
     grammar = re.compile(r"\d+")
     
class ArithmeticOperands(str):
    grammar = re.compile(r"[\(\)\+\-\*\/]")
    
class ParenthesesMatch(str):
    grammar =re.compile(r"([\(\)])")
    
class LogicOperands(Symbol):
    grammar = Enum( K("OR"), K("AND") , K("NOT") )
    
class ComparatorOperands(Symbol):
    grammar =Enum(K(">"),K("<"),K(">="),K("<="),K("!="),K("==="))
    
class Print(str):
    grammar = "print","(",[word,Digit,String,BoolLiteral,Identifier],")",";"
    
class ArithmeticBinaryOperation(str):
        grammar = [ParenthesesMatch,'' ],[Digit,Identifier], [ArithmeticOperands] , [Digit,Identifier],[ParenthesesMatch,'']

class Assignment(str):
    grammar = attr("type", Type), attr("identifier",Identifier ), ":=" , attr("expression", String) , ";"
    

stringToParse = "(5  + 5 )"
f = parse(stringToParse,ArithmeticBinaryOperation)
print(f)


"""

"""    
stringToParse = "String myFirstVariable:=  \"escaped quote\" ;"
f = parse(stringToParse, Assignment)

print(f.type)
print(f.identifier)
print(f.expression)

"""