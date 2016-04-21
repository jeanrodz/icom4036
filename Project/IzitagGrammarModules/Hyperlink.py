#from __future__ import unicode_literals, print_function
#from builtins import range
import re
#from macpath import split
from pip._vendor.pyparsing import empty
#from lib2to3.fixer_util import String

def hyper_checker(string, string_collection):
    
    pos_list = []
    start_list = []
    subs_list = []
    end_list = []
    length = 0
    new_strings = []
    new_string = ""

    for m in re.finditer('iziHyper\(', string):
        pos_list.append(m.end())
        start_list.append(m.start()) 
    
    if (start_list is empty) : print ("FU")
    else: 
        for i in range(0, len(pos_list)):
            ahhh = ""
            substring = []
            subs = []
            for j in range(pos_list[i], len(string)):
                if (string[j] == ")"):
                    end_list.append(j)
                    break
                else :
                    substring.append(string[j])
    
            subs.append(ahhh.join(substring))
            subs_list.append(subs)

        if (end_list is empty) : print("UR FCE")
        else:
            for element in subs_list :
                line = element[0]
                nl = line.replace("'", "")
                nl = nl.split(", ")
                nl[0].replace(" ", "")
                nl[1].replace(" ", "")
                
                if ((nl[0] not in string_collection) | (nl[1] not in string_collection)) : 
                    print("ERROR!")
                    break
    
                else : 
                    ns = "<a href=\"" + string_collection.get(nl[1]) + "\">" + string_collection.get(nl[0]) + "</a>"            
                    new_string = ns
                    
                    length = len(ns) - len(string)

            string1 = string
            pos1 = 0
            pos2 = 0
                
            for i in range(0, len(start_list)):
                pos1 = start_list[i]
                pos2 = end_list[i]

                size = len(string) - len(string1)
                string1 = string1[:pos1-size] + new_string + string1[pos2+1-size:]
                size = len(string) - len(string1)
                
            return string1
        




