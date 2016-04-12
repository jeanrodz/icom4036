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
    
#def list_function(nl):
 #   if (nl[2] == "ordered"):
  #      for (i = )

def load_tokens(file): 
    with open(file,"rt") as in_file:
        for line in in_file:
            newline = line.replace("\n","")
            nl = newline.replace("[","")
            nl = nl.replace("]","")
            nl = nl.replace("'","")
            nl = nl.split(", ")
            
            if ((nl[0] == 'int') & (nl[1] not in int_collection)): int_collection[nl[1]] = nl[2]
            elif ((nl[0] == 'string') & (nl[1] not in string_collection)): string_collection[nl[1]] = nl[2] 
            elif ((nl[0] == 'float') & (nl[1] not in float_collection)): float_collection[nl[1]] = nl[2]
            elif ((nl[0] == 'array') & (nl[1] not in array_collection)): array_collection[nl[1]] = nl[2]
            elif ((nl[0] == 'iziTitle') & (nl[1] in string_collection)): title_function(nl)
            elif (nl[0] == 'iziSection'): section_function(condition)
            elif ((nl[0] == 'iziParagraph') & (nl[1] in string_collection)): paragraph_function(nl)
           # elif ((nl[0] == 'iziList') & (nl[1] in array_collection)): list_function(nl)      
            token_stack.append(nl)
                      

load_tokens('source.txt')  

print(int_collection)
print(string_collection)
print(float_collection)
print(array_collection)

"""
Data Definitions
"""
#current_token = token_stack[1]


"""
Parse-Map Dictionary
"""
"""    
for index in range(0, len(token_stack)):
    current_token = token_stack[index]

    def data_type_assignment(current_token):
        #print(current_token)
        if(current_token[0] == 'int'): int_collection[current_token[1]] = current_token[2]
        
        elif (current_token[0] == 'float'): float_collection[current_token[1]] = current_token[2]
        
        elif ((current_token[0] == 'iziTitle') & (current_token[1] in string_collection)): title_function(current_token)
        
        else : string_collection[current_token[1]] = current_token[2]
        
    def title_function(current_token):
        title_collection["title"] = string_collection.get(current_token[1])

    parse_map = {
        'int' : data_type_assignment(current_token),
        'string' : data_type_assignment(current_token),
        'float' : data_type_assignment(current_token),
        'iziTitle' : data_type_assignment(current_token),
        }

#print (int_collection)
#print (string_collection)
#print (float_collection)
#print (title_collection)
"""
"""
print(token_stack)
print(string_collection)
print(int_collection)
print(float_collection)
"""
