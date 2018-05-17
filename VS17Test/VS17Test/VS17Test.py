# import is used to make specialty functions available
# These are called modules
import random
import sys
import os

#print("Hello World")

#Comments
'''
multiline comments
'''
# A variable is a place to store values
# Its name is like a label for that value
#var1 = "Michael"
#print(var1)

#single or double quotes
# A variable name can contain letters, numbers, or _, but can't start with a number
# Five main data types in python: numbers, strings, lists, tuples, dictionaries (maps)
# You can store any of them in the same variable.
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
#A string is a string of characters surrounded by " or '
#string has escape char of \, and there is no ; at end of line.
#var2 = "\"Michael\"" 
#python uses _ between names in varables as convention.
#multi_line_quote = ''' just
#like everyone else'''
#concatenate strings below type 1.
#new_string = var2 + multi_line_quote
#print(new_string)
#concatenate strings below type 2.
#print("%s %s %s" %("I like quotes", multi_line_quote, var2))
#How to print to screen without new line showing up every time. Or anther way: To keep from printing newlines use end=""
#print("I don't like", end="")
#print(" line breaks.")
#If you want a new line it is \n 
#You can print a string multiple times with *
#print("\n" *5)

#list: a list of values and you can manipulate them. Each one will have an
#index, and it is zero based. Index is its map coordinate or label to find them. 
#everything will fit in a list, strings, numbers any data type you like..
#grocery_list = ["Potatoes", "Juice", "Bananas", "Meat"]
#print("First Item: ", grocery_list[0])
#Change value of first item
#grocery_list[0] = "Apples"
#print("First Item: ", grocery_list[0])
#Can print just subset of list. Will print up to but not inclue last number.
#You can get a subset of the list with [min:up to but not including max]
#print("List items (zero based) 1-3:", grocery_list[1:3])
#You can put in other things like a list of lists. 
#other_events = ["Wash car", "Get paid", "Have sex"]
#to_do_list = [other_events, grocery_list]
#print(to_do_list)
#lists are boxes inside of boxed.
#if we wanted 3rd item from list we would select 2nd array, and 2 item in it. Zero based so 1, and 2
#print((to_do_list[1][2]))
#you can append list.
#grocery_list.append("Steak")
#Insert in a specific index.
#grocery_list.insert(1, "Sex lube")
#remove from a specific index
#grocery_list.remove("Juice")
#sort
#grocery_list.sort()
#reverse
#grocery_list.reverse()
#delete item.
#del grocery_list[3]
#now print off list, and notice that it changed to_do_list
#print(to_do_list)

# We can combine lists with a +
#to_do_list = other_events + grocery_list
#print(to_do_list)

# Get length of list
#print(len(to_do_list))

# Get the max item in list, what ever is highest alphabetically.
#print(max(to_do_list))

# Get the minimum item in list, or first alphabetically.
#print(min(to_do_list))

# TUPLES -------------
# Values in a tuple can't change like lists.
#Tuples are ordered set of values comma seperated. They are immutable in python, and use () not [].
#Other than that they are like lists. Used when you have data you don't want easily changed. 
#If you want to change it, most people change to list, then change, then change back to tuple. Not normally done.
#pi_tuple = (3, 1, 4, 1, 5, 9)

# Convert tuple into a list
#new_tuple = list(pi_tuple)

# Convert a list into a tuple
# new_list = tuple(grocery_list)

# tuples also have length: len(tuplevar1), min(tuplevar1) and max(tuplevar1)
#Notice that you are passing in the tuple's name. Above is just example.

# DICTIONARY or MAP -------------
# Made up of values with a unique key for each value. Key value pair.
# Similar to lists, but you can't join dictionaries like you can list with a +
#Notice that list is[], tuples is (), and dictionary is {}

#super_villains = {'Fiddler' : 'Isaac Bowin',
#                  'Captain Cold' : 'Leonard Snart',
#                  'Weather Wizard' : 'Mark Mardon',
#                  'Mirror Master' : 'Sam Scudder',
#                  'Pied Piper' : 'Thomas Peterson'}

#print(super_villains['Captain Cold'])

# Delete an entry
#del super_villains['Fiddler']
#print(super_villains)

# Replace a value
#super_villains['Pied Piper'] = 'Hartley Rathaway'

# Print the number of items in the dictionary, Length
#print(len(super_villains))

# Get the value for the passed key, remember this is a key value pair. 
#print(super_villains.get("Pied Piper"))

# Get a list of dictionary keys
#print(super_villains.keys())

# Get a list of dictionary values
#print(super_villains.values())

# CONDITIONALS -------------
# The if, else and elif statements are used to perform different
# actions based off of conditions
# Comparison Operators : ==, !=, >, <, >=, <=

# The if statement will execute code if a condition is met
# White space is used to group blocks of code in Python
# Use the same number of proceeding spaces for blocks of code

#age = 30
#if age > 16 :
#    print('You are old enough to drive')

# Use an if statement if you want to execute different code regardless
# of whether the condition ws met or not

#if age > 16 :
#    print('You are old enough to drive')
#else :
#    print('You are not old enough to drive')

# If you want to check for multiple conditions use elif
# If the first matches it won't check other conditions that follow

#if age >= 21 :
#    print('You are old enough to drive a tractor trailer')
#elif age >= 16:
#    print('You are old enough to drive a car')
#else :
#    print('You are not old enough to drive')

# You can combine conditions with logical operators
# Logical Operators : and, or, not

#if first one is met, nothing else will be checked.
#if ((age >= 1) and (age <= 18)):
#    print("You get a birthday party")
#elif (age == 21) or (age >= 65):
#    print("You get a birthday party")
#notice that elif not(stuff) does the opposite of what ever. 
#elif not(age == 30):
#    print("You don't get a birthday party")
#else:
#    print("You get a birthday party yeah")

# FOR LOOPS -------------
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9, not to 10.
#for x in range(0, 10):
#    print(x , ' ', end="")

#print('\n')

# You can use for loops to cycle through a list
#grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']


#for y in grocery_list:
#    print(y)

## You can also define a list of numbers to cycle through
#for x in [2,4,6,8,10]:
#    print(x)

# You can double up for loops to cycle through lists
#num_list =[[1,2,3],[10,20,30],[100,200,300]];

#for x in range(0,3):
#    for y in range(0,3):
#        print(num_list[x][y])

# WHILE LOOPS -------------
# While loops are used when you don't know ahead of time how many
# times you'll have to loop
#remember we had to import the random speciality function. 
random_num = random.randrange(0,100)

#this will cycle through til condition is met. Will go til it is not = 15.
#while (random_num != 15):
#    print(random_num)
#    random_num = random.randrange(0,100)

# An iterator for a while loop is defined before the loop
#i = 0;
#while (i <= 20):
#    if(i%2 == 0):
#        print(i)
#    elif(i == 9):
#        # Forces the loop to end all together
#        break
#    else:
#        # Shorthand for i = i + 1
#        i += 1
#        # Skips to the next iteration of the loop
#        continue

#    i += 1

# FUNCTIONS -------------
# Functions allow you to reuse and write readable code
# Type def (define), function name and parameters it receives
# return is used to return something to the caller of the function
# Same as a method but method is in class, function is by itself. 
# def function name(paramters it will recieve.)
# actual function, 
# retrun varable name. 
#def addNumbers(fNum, sNum):
#    sumNum = fNum + sNum
#    return sumNum
#sumNum is not avalible outside of function, it is out of scope. 

#print(addNumbers(1, 4))

#you can make it a string and it will work in the same way.
#myaddnumberstring = addNumbers(1, 4)

# Can't get the value of rNum because it was created in a function
# It is said to be out of scope
# print(sumNum)

# If you define a variable outside of the function it works every place
#newNum = 0;
#def subNumbers(fNum, sNum):
#    newNum = fNum - sNum
#    return newNum

#print(subNumbers(1, 4))

# USER INPUT -------------
#print('What is your name?')

# Stores everything typed up until ENTER. Notice that sys is being used. 
#standardin
#name = sys.stdin.readline()

#print('Hello', name)

# STRINGS -------------
# A string is a series of characters surrounded by ' or "
#long_string = "I'll catch you if you fall - The Floor"

# Retrieve the first 4 characters
#print(long_string[0:4])

# Get the last 5 characters
#print(long_string[-5:])

# Everything up to the last 5 characters
#print(long_string[:-5])

# Concatenate part of a string to another
#print(long_string[:4] + " be there")

# String formatting, %c is a charater, %s is string, %d is signed integer and .5f is floating with at least 5 decimal places. Why is las % there?  
#print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14))

# Capitalizes the first letter
#print(long_string.capitalize())

# Returns the index of the start of the string
# case sensitive, has to be exactly the same. 
#print(long_string.find("Floor"))

# Returns true, if all characters are all letters. (' isn't a letter)
#print(long_string.isalpha())

# Returns true if all characters are numbers
#print(long_string.isalnum())

# Returns the string length
#print(len(long_string))

# Replace the first word with the second (Add a number to replace more)
#print(long_string.replace("Floor", "Ground"))

# Remove white space from front and end
#print(long_string.strip())

# Split a string into a list based on the delimiter you provide. In this case a space.
#quote_list = long_string.split(" ")
#print(quote_list)

# FILE I/O -------------Input Output. 

# Overwrite or create a file for writing
#not sure what he means by sending wb as command. 
#test_file = open("test.txt", "wb")


#Use ab+ to read and append to file. It also opens or create the file. 

# Get the file mode used
#print(test_file.mode)

# Get the files name
#print(test_file.name)

# Write text to a file with a newline
#test_file.write(bytes("Write me to the file\n", 'UTF-8'))

# Close the file
#test_file.close()

# Opens a file for reading and writing
#test_file = open("test.txt", "r+")

# Read text from the file
#text_in_file = test_file.read()

#print(text_in_file)

# Delete the file. 
#This is where OS module comes in. 
#os.remove("test.txt")

# CLASSES AND OBJECTS -------------
# The concept of OOP allows us to model real world things using code
# Every object has attributes (color, height, weight) which are object variables
# Every object has abilities (walk, talk, eat) which are object functions

class Animal:
    # None signifies the lack of a value
    # You can make a variable private by starting it with __
    #none is lack of a value, or you can use "" (empty quotes.)
    #two _ means that these variables are private. 
    #__name = None
    #__height = None
    #__weight = None
    #__sound = None

    # The constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class
    # Has 2 underscores and initilize, then 2 more undersocres.
    # Remember that they left side of equal sign is what they passed in.  
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

        #this is setter, and set name self allows object to refer to it self. Asks if name is valid and if so it will set it. 
    #def set_name(self, name):
    #    self.__name = name

    #def set_height(self, height):
    #    self.__height = height

    #def set_weight(self, height):
    #    self.__height = height

    #def set_sound(self, sound):
    #    self.__sound = sound

    #def get_name(self):
    #    return self.__name

    #def get_height(self):
    #    return str(self.__height)

    #def get_weight(self):
    #    return str(self.__weight)

    #def get_sound(self):
    #    return self.__sound

    #def get_type(self):
    #    print("Animal")

        #{} is a place holder to put information in a location.
        #bc we are inside of class we don't need to use getters and setters to refere to the values in these variables.   
    #def toString(self):
    #    return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)

# How to create a Animal object
#cat = Animal('Whiskers', 33, 10, 'Meow')

#print(cat.toString())

# You can't access this value directly because it is private
#print(cat.__name)

# INHERITANCE -------------
# You can inherit all of the variables and methods from another class

#class Dog(Animal):
#    __owner = None

#    def __init__(self, name, height, weight, sound, owner):
#        self.__owner = owner
#        self.__animal_type = None

        # How to call the super class constructor which is animal from above.
    #    super(Dog, self).__init__(name, height, weight, sound)

    #def set_owner(self, owner):
    #    self.__owner = owner

    #def get_owner(self):
    #    return self.__owner

    #def get_type(self):
    #    print ("Dog")

    # We can overwrite functions in the super class
    #def toString(self):
    #    return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(), self.get_height(), self.get_weight(), self.get_sound(), self.__owner)

    # You don't have to require attributes to be sent
    # This allows for method overloading. Method overloading allows different tasks depending on what is passed in. 
#    def multiple_sounds(self, how_many=None):
#        if how_many is None:
#            print(self.get_sound)
#        else:
#            print(self.get_sound() * how_many)

#spot = Dog("Spot", 53, 27, "Ruff", "Derek")

#print(spot.toString())

# Polymorphism allows use to refer to objects as their super class
# and then automaticly have their correct functions called automatically

#class AnimalTesting:
#    def get_type(self, animal):
#        animal.get_type()

#test_animals = AnimalTesting()

#test_animals.get_type(cat)
#test_animals.get_type(spot)

#spot.multiple_sounds(4)
#just adding stuff to make new install work.