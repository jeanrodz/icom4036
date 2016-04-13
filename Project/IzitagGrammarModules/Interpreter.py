from __future__ import unicode_literals, print_function
from yattag import Doc


"""
/*****************************************************
Module Description: Here we will use the dictionaries for the state machine :)
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
outpath = "index.html"

with open (outpath, "wt") as outfile:
    outfile.write("<!DOCTYPE html>\n")
    outfile.write("<html>\n")
    outfile.write("<head>\n")
    outfile.write("</head>\n")
    outfile.write("<body>\n")
    outfile.write("</body>\n")
    outfile.write("</html>\n")
    outfile.close()
"""

doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        with tag('title'):
            text('Hello world!')
    with tag ('body'):
        text('Hello world!')
    
outpath = "index.html"

with open (outpath, "wt") as outfile:
    outfile.write(doc.getvalue())
    outfile.close()
            
def title_function(nl):
    print("<title>" + string_collection.get(nl[1]) + "</title>")

def section_function(condition):
    if (condition == True): print("</section>" + "<section>")
    else : 
        print("<section>")
        condition = True

def paragraph_function(nl):
    print("<p>" + string_collection.get(nl[1]) + "</p>")
    '''
    with tag('p'):
        text(string_collection.get(nl1))
    '''
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
        print("<ol>");
        for i in range(0, len(list_items)): print("<li>" + list_items[i] + "</li>")
        print("</ol>")
        
    elif (nl[1] == "unordered"): 
        print("<ul>")
        for i in range(0, len(list_items)): print("<li>" + list_items[i] + "</li>")
        print("</ul>")
    
    else : print("WHAT KIND OF LIST ARE YOU TRYING TO DO?!")
        
def add_array(nl):
    array_items = []
    for i in range(2, len(nl)):
        array_items.append(nl[i])
    
    array_collection[nl[1]] = array_items
    print(array_collection)

def table_function(nl):
    print("Jean is going to do this part!!")    

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

def load_tokens(file): 
    with open(file,"rt") as in_file:
        for line in in_file:
            newline = line.replace("\n","")
            if (newline == "iziSection") : newline = "['iziSection', '']"
            if (newline == "") : break
            nl = newline.replace("[","")
            nl = nl.replace("]","")
            nl = nl.replace("'","")
            nl = nl.split(", ")
            
            instruction_checker(nl)   
            
            token_stack.append(nl)

load_tokens('source.txt')  

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
        
#print(section_stack)               
        
#print(int_collection)
#print(string_collection)
#print(float_collection)
#print(array_collection)



