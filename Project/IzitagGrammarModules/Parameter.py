from __future__ import unicode_literals, print_function
from pypeg2 import *
from DataTypes import *
from Identifier import *
from Assignment import *


class Parameter(str):
    grammar =  [FloatLiteral,IntLiteral,StringLiteral,Identifier]
    
    
class Parameters(str):
   grammar = optional(csl(Parameter))
    
