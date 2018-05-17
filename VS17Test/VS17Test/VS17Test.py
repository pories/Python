import random
import sys

#print("Hello World")

#Comments
'''
multiline comments
'''
var1 = "Michael"
#print(var1)
#single or double quotes
#variable stores values. Has to start with a letter, then it can numbers or _.
# Five main data types in python: numbers, strings, lists, tuples, dictionaries (maps)
# Seven math types: +,-,*,/,%, ** (exponential), and // (floor devision, discards remainder and rotates down. 14.5 goes to 14.)
#Notice that the string in print is seperated by comma and then expression.
#print("5+2= ", 5+2 )
#print("5-2= ", 5-2)
#print("5*2= ", 5*2)
#print("5/2= ", 5/2)
#print("5%2= ", 5%2)
#print("5**2= ", 5**2)
#print("5//2= ", 5//2)
#Mathmatical order of operation is pemdas, use () to make things right. 
#string has escape char of \, and there is no ; at end of line.
var2 = "\"Michael\"" 
#python uses _ between names in varables as convention.
multi_line_quote = ''' just
like everyone else'''
#concatenate strings below type 1.
#new_string = var2 + multi_line_quote
#print(new_string)
#concatenate strings below type 2.
#print("%s %s %s" %("I like quotes", multi_line_quote, var2))
#How to print to screen without new line showing up every time.
#print("I don't like", end="")
#print(" line breaks.")
#If you want a new line it is \n 
#To print 5 new lines
#print("\n" *5)

#list: a list of values and you can manipulate them. Each one will have an
#index, zero based. Index is its map coordinate or label to find them. 
#everything will fit in a list, strings, numbers any data type you like..
grocery_list = ["Potatoes", "Juice", "Bananas", "Meat"]
#print("First Item: ", grocery_list[0])
#Change value of first item
#grocery_list[0] = "Apples"
#print("First Item: ", grocery_list[0])
#Can print just subset of list. Will print up to but not inclue last number.
#print("List items (zero based) 1-3:", grocery_list[1:3])
#You can put in other things like a list of lists. 
other_events = ["Wash car", "Get paid", "Have sex"]
to_do_list = [other_events, grocery_list]
print(to_do_list)
#lists are boxes inside of boxed.
#if we wanted 3rd item from list we would select 2nd array, and 2 item in it. Zero based so 1, and 2
print((to_do_list[1][2]))
#you can append list.
grocery_list.append("Steak")
#