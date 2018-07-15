'''
Following derek banas video:
https://www.youtube.com/watch?v=N4mEzFDjqtA
'''

import random
import sys
import os

print ("Hello world")

# this is a comment

'''
multi line comment

'''

name = 'Mike'
print(name)

# escape character
name2 = "\"This is a quote\""
print(name2)

string1 = "1"
string2 = "2"

# embedded strings
print("here are some strings %s %s" % (string1, string2))

# list
climbing_essentials_list = ["harness", "rock shoes", "chalk bag", "belay device"]

print(climbing_essentials_list)
# print elements 1-4
print(climbing_essentials_list[1:4])

# we can nest lists inside of lists in a similar way

# append
climbing_essentials_list.append("cams")

# delete
del climbing_essentials_list[2]
climbing_essentials_length = climbing_essentials_list.__len__()

print("We have %s items in our climbing list" % climbing_essentials_length)

# tuples - immutable
mike_tuple = (1,2,3)

# dictionary / map
pizza = {
    'name' : 'margherita',
    'ingredients' : 'cheese, tomato',
    'rating' : 5
}

print(pizza['name'])

price_of_drink = 5
funds = 4
barkeeper_mood = "happy" #"moody"

# conditionals
if funds >= price_of_drink :
    print("Enjoy your drink")
elif funds == price_of_drink -1 and barkeeper_mood != "moody":
    print("I'm feeling generous - have a drink anyway")
else:
    print("Please come back with more money")

# for loops

for x in range(0,10) :
    print(x)

for y in climbing_essentials_list :
    print(y)

while_max = 0
while while_max <= 5:
    print("Not got to while_max yet")
    while_max +=1

def add_number(some_num, another_num):
    some_num  = some_num + another_num
    return some_num

print(add_number(4,2))

class Car :
    
    # private class properties (static)
    __i = 1

    # constructor
    def __init__(self, model, brand):
        self.__model = model
        self.__brand = brand
        self.__name = "abu"

    # get private class property
    @property
    def i(cls):
        return cls.__i

    # setter methods
    def set_model(self, model):
        self.__model = model
    
    def set_brand(self, brand):
        self.__brand = brand
    
    @property
    def model(self) :
        return self.__model

    @property    
    def brand(self) :
        return self.__brand
    
    @property
    def name(self):
        return self.__name
    
    @staticmethod
    def make_sound() :
        print("vroom vroom")

    @name.setter
    def name(self, name):
        self.__name = name


print("This is mike's car")
mikes_car = Car("corsa", "vauxhall")
mikes_car.name = "karen"
print(mikes_car._Car__name)
print(mikes_car.name)
print(mikes_car.i)

print("This is simon's car")
simons_car = Car("sportage","kia")
print(simons_car.model)
print(simons_car.brand)
print(simons_car.i)
Car.make_sound()