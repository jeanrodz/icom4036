from __future__ import unicode_literals, print_function
from yattag import Doc
from yattag import indent


"""
/*****************************************************
Stacks and Collections
/*****************************************************
"""

token_stack = []
int_collection = {}
float_collection = {}
string_collection = {}
array_collection = {}
title_collection = {}
section_stack = []

condition = False

"""
/*****************************************************
Intermediate Code Functions and Analysis
/*****************************************************
"""

doc, tag, text = Doc().tagtext()
            
def title_function(nl):
    with tag('head'):
        with tag ('title'):
            text(string_collection.get(nl[1]))
    
def paragraph_function(nl):  
    with tag('p'):
        text(string_collection.get(nl[1]))
    
def iziImage(source, height, width):
    if ((height in int_collection) or (height in float_collection)) & ((width in int_collection) or (width in float_collection)):
    
        if (height in int_collection): imgheight = int_collection.get(height)
        else : imgheight = float_collection.get(height)
    
        if (width in int_collection): imgwidth = int_collection.get(width)
        else : imgwidth = float_collection.get(width)
    
        print("<img src='" + source + "' height='" + imgheight + "'" + " width='" + imgwidth + "'>")
    
    else : print("S#!T")
    
def list_function(nl):
    list_items = array_collection.get(nl[2])  

    if (nl[1] == "ordered"):
        with tag('ol'): 
            for i in range(0, len(list_items)): 
                with tag('li'):     
                    text(list_items[i])
               
    elif (nl[1] == "unordered"): 
        with tag('ul'):
            for i in range(0, len(list_items)): 
                with tag('li'):
                    text(list_items[i])
            
    else : print("WHAT KIND OF LIST ARE YOU TRYING TO DO?!")
        
def add_array(nl):
    array_items = []
    for i in range(2, len(nl)):
        array_items.append(nl[i])
    
    array_collection[nl[1]] = array_items

def table_function(nl):
    with tag('table'):
        with tag('tr'):
            with tag('th'):
                text(string_collection.get(nl[1]))
                for row_index in range(2, len(nl)):
                    with tag('tr'):
                        row = array_collection[nl[row_index]]
                        for item in row:
                            with tag('td'):
                                text(item)

def instruction_checker(nl):
    if ((nl[0] == 'int') & (nl[1] not in int_collection)): int_collection[nl[1]] = nl[2]
    elif ((nl[0] == 'string') & (nl[1] not in string_collection)): string_collection[nl[1]] = nl[2] 
    elif ((nl[0] == 'float') & (nl[1] not in float_collection)): float_collection[nl[1]] = nl[2]
    elif ((nl[0] == 'array') & (nl[1] not in array_collection)): add_array(nl)
    elif ((nl[0] == 'iziTitle') & (nl[1] in string_collection)): title_function(nl)
    elif ((nl[0] == 'iziImage') & (nl[1] in string_collection)): iziImage(string_collection.get(nl[1]), nl[2], nl[3])
    elif ((nl[0] == 'iziParagraph') & (nl[1] in string_collection)): paragraph_function(nl)
    elif ((nl[0] == 'iziList') & (nl[2] in array_collection)): list_function(nl) 
    elif ((nl[0] == 'iziTable') & (nl[1] in string_collection)): table_function(nl)  


"""
/*****************************************************
File Reader and Stack Creator
/*****************************************************
"""

def load_tokens(file): 
    found_section = False
    
    with open(file,"rt") as in_file:
        for line in in_file:
            newline = line.replace("\n","")
            if (newline == "iziSection") : 
                newline = "['iziSection', '']"
                found_section = True
                
            if (newline == "") : break
            nl = newline.replace("[","")
            nl = nl.replace("]","")
            nl = nl.replace("'","")
            nl = nl.split(", ")
            
            if (found_section) : token_stack.append(nl)
            else : instruction_checker(nl)
            
load_tokens('source.txt')

print (token_stack)

for i in range(0, len(token_stack)):
    token = token_stack[i]
    if token[0] == 'iziSection':
        section = [ ]
        for j in range(i+1, (len(token_stack))):
            temp_token = token_stack[j]
            if(temp_token[0] != 'iziSection'):
                section.append(temp_token)
            else:
                break
        section_stack.append(section)
        
print(section_stack)

"""
/*****************************************************
HTML Doc Generation
/*****************************************************
"""               

doc.asis('<!DOCTYPE html>')
with tag('html'):       
    with tag ('body'):
        for i in range(0, len(section_stack)):
            with tag ('section', class='{}'.format(section_stack[i][1])):
                text('\n')
                for element in section_stack[i]:
                    print (element)
                    instruction_checker(element)
                    

result = indent(doc.getvalue(), indentation = '', newline = '\r\n')
    
outpath = "index.html"

with open (outpath, "wt") as outfile:
    outfile.write(result)
    outfile.close()   
        




