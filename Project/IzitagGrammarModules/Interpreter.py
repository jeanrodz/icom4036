from __future__ import unicode_literals, print_function
from yattag import Doc
from yattag import indent
from pydoc import doc
import ParseOutputGen
#from test.support import temp_cwd
from Hyperlink import *


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
        #text(string_collection.get(nl[1]))
        doc.asis(string_collection.get(nl[1]))
    
def iziImage(source, height, width):
    if ((height in int_collection) or (height in float_collection)) & ((width in int_collection) or (width in float_collection)):
    
        if (height in int_collection): imgheight = int_collection.get(height)
        else : imgheight = float_collection.get(height)
    
        if (width in int_collection): imgwidth = int_collection.get(width)
        else : imgwidth = float_collection.get(width)
        
        with tag('img'):
            doc.attr(src = source, height = imgheight, width = imgwidth)
    
    else : print("S#!T")
    
def list_function(nl):
    list_items = array_collection.get(nl[2])  
    print(list_items)
    
    if (nl[1] == "ordered"):
        with tag('ol'): 
            for i in range(0, len(list_items)): 
                with tag('li'):     
                    #text(list_items[i])
                    doc.asis(list_items[i])
               
    elif (nl[1] == "unordered"): 
        with tag('ul'):
            for i in range(0, len(list_items)): 
                with tag('li'):
                    #text(list_items[i])
                    doc.asis(list_items[i])
            
    else : print("WHAT KIND OF LIST ARE YOU TRYING TO DO?!")
        
def add_array(nl):
    array_items = []
    jump = False
    for i in range(2, len(nl)):
        if (jump == False):
            if (nl[i].find("iziHyper(") >= 0):
                temp_list = []
                temp = ""
                
                temp_list.append(nl[i])
                temp_list.append(", ")
                temp_list.append(nl[i+1])
                temp = temp.join(temp_list)
                
                result = hyper_checker(temp, string_collection)
                array_items.append(result)
                
                jump = True
            
            else : array_items.append(nl[i])
        
        else :
            jump = False
    
    array_collection[nl[1]] = array_items
    
def hyper_function(alias, url):
    with tag('a'):
        doc.attr(href = url)
        text(alias)

def add_string(nl):
    string_list = []
    temp_string = ""
    
    if (len(nl) > 2) : 
        string_list.append(nl[2])
        for i in range(3, len(nl)):
            string_list.append(', ')
            string_list.append(nl[i])
    
    else : string_list.append(nl[i])

    temp_string = temp_string.join(string_list)
    
    result = hyper_checker(temp_string, string_collection)
    string_collection[nl[1]] = result
    
    #string_collection[nl[1]] = temp_string
    
def table_function(nl):
    with tag('table'):
        with tag('tr'):
            with tag('th'):
                #text(string_collection.get(nl[1]))
                doc.asis(string_collection.get(nl[1]))
                for row_index in range(2, len(nl)):
                    with tag('tr'):
                        row = array_collection[nl[row_index]]
                        for item in row:
                            with tag('td'):
                                #text(item)
                                doc.asis(item)

def instruction_checker(nl):
    if ((nl[0] == 'int') & (nl[1] not in int_collection)): int_collection[nl[1]] = nl[2]
    elif ((nl[0] == 'string') & (nl[1] not in string_collection)): add_string(nl) 
    elif ((nl[0] == 'float') & (nl[1] not in float_collection)): float_collection[nl[1]] = nl[2]
    elif ((nl[0] == 'array') & (nl[1] not in array_collection)): add_array(nl)
    elif ((nl[0] == 'iziTitle') & (nl[1] in string_collection)): title_function(nl)
    elif ((nl[0] == 'iziImage') & (nl[1] in string_collection)): iziImage(string_collection.get(nl[1]), nl[2], nl[3])
    elif ((nl[0] == 'iziPar') & (nl[1] in string_collection)): paragraph_function(nl)
    elif ((nl[0] == 'iziList') & (nl[2] in array_collection)): 
        print ("list found")
        list_function(nl) 
    elif ((nl[0] == 'iziTable') & (nl[1] in string_collection)): table_function(nl)  
    elif ((nl[0] == 'iziHyper') & (nl[1] in string_collection) & (nl[2] in string_collection)): 
            hyper_function(string_collection.get(nl[1]), string_collection.get(nl[2]))


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
            #if (newline == "iziSection") : 
            #    newline = "['iziSection', '']"
            #    found_section = True
                
            if (newline == "") : break
            nl = newline.replace("[","")
            nl = nl.replace("]","")
            nl = nl.replace("'","")
            
            #nl = nl.replace("&", "&amp;")
            #nl = nl.replace("<", "&lt;")
            #nl = nl.replace(">", "&gt;")

            nl = nl.split(", ")
            if (nl[0] == "iziSection") : found_section = True
             
            if (found_section) : token_stack.append(nl)
            else : instruction_checker(nl)

"""
/*****************************************************
HTML Doc Generation
/*****************************************************
""" 

def main():
    doc.asis('<!DOCTYPE html>')
    with tag('html'):       
        with tag ('body'):
            load_tokens('source.txt')
            section_id = []

            for i in range(0, len(token_stack)):
                token = token_stack[i]
                if token[0] == 'iziSection':
                    section = [ ]
                    id = token[1]
                    print(id)
                
                    for j in range(i+1, (len(token_stack))):
                        temp_token = token_stack[j]
                        if(temp_token[0] != 'iziSection'):
                            section.append(temp_token)
                        else:
                            break
                    
                    section_stack.append(section)
                    section_id.append(id)
                    print(section_id)

            counter = 0
            for j in range(0, len(section_stack)):
                section_class = token_stack[j]
            
                if (section_id[counter] not in string_collection) : print("stop bullshitting!")
                else :
                    print(string_collection.get(section_id[counter]))
                    with tag ('section', klass = string_collection.get(section_id[counter])):
                        text('\n')
                        for element in section_stack[j]:
                        
                            instruction_checker(element)                         
                    counter = counter + 1
            
    result = indent(doc.getvalue(), indentation = '', newline = '\r\n')
    
    outpath = "index.html"

    with open (outpath, "wt") as outfile:
        outfile.write(result)
        outfile.close()   

if __name__ == '__main__': 
    main()
    print("Main is working.")