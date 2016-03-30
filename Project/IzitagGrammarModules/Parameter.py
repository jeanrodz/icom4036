from __future__ import unicode_literals, print_function
from pypeg2 import *
from DataTypes import *
from Identifier import *
from Assignment import *


class Parameter(str):
    grammar =  [FloatLiteral,IntLiteral,StringLiteral,Identifier]
    
    
class Parameters(List):
   grammar = optional(csl(Parameter))
    
test = "6.7,88,'IamAString',IamAIdentifier"
f = parse(test,Parameters)

print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(len(f)) 