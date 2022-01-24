#Week 1

#args ///////////////////////////////////////////////////////////////
#def addition(*args):
   #result = 0
   #for i in args:
  #    result += i
 #  return result
#print(addition(1,4))
#5
#print(addition(1,7,3))
#11

#kwargs /////////////////////////////////////////////////////////////
#def arg_printer(a, b, option=True, **kwargs):
 #  print(a, b)
  # print(option)
   #print(kwargs)
#arg_printer(3, 4, param1=5, param2=6)
#3 
#4
#true
#{'param1': 5, 'param2': 6}

#lists ////////////////////////////////////////////////////////////////////
#words = ['data','science'] #create a list
#print(words[0]) #access an item
#'data'
#words.append('machine') #add an item
#print(len(words)) #length of list
#3
#print(words)
#['data', 'science', 'machine']

#Grades ///////////////////////////////////////////////////////////////////
#grades = {'John':'A', 'Emily':'A+', 'Betty':'B', 'Mike':'C', 'Ashley':'A'}

#grades['John']
#'A'
#grades.get('Betty')
#'B'

#tuples ////////////////////////////////////////////////////////////////////////
#a = ('3', '4')
#print(type(a))

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Week 2

#if or else ////////////////////////////////////////////////////////////////////////
#a = 200
#b = 33
#if b > a:
#  print("b is greater than a")
#elif a == b:
#  print("a and b are equal")
#else:
#  print("a is greater than b")

#While loops ////////////////////////////////////////////////////////////////////////
#i = 1
#while i < 6:
#  print(i)
#  i += 1
#else:
#  print("i is no longer less than 6")

#For Loops //////////////////////////////////////////////////////////////////////////
#adj = ["red", "big", "tasty"]
#fruits = ["apple", "banana", "cherry"]

#for x in adj:
#  for y in fruits:
#    print(x, y)

#Arrays /////////////////////////////////////////////////////////////////////////////
#cars = ["Ford", "Volvo", "BMW"]
#cars[0] = "Toyota"
#x = cars[0]
#x = len(cars)
#cars.append("Honda")
#cars.pop(1)
#cars.remove("Volvo")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Week 3 

# Dates
#import datetime

#x = datetime.datetime.now()
#print(x)

#/////////////////////////////////////////////////////////////////////////////////

#Maths
#x = min(5, 10, 25)
#y = max(5, 10, 25)

#print(x)
#print(y)

#///////////////////////////////////////////////////////////////////////////////////
#Python JSON (can work with json  data)
#import json

# some JSON:
#x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
#y = json.loads(x)

# the result is a Python dictionary:
#print(y["age"])

#//////////////////////////////////////////////////////////////////////////////////////
#Python RegEx Rgular Expression
#import re

#Check if the string starts with "The" and ends with "Spain":

#txt = "The rain in Spain"
#x = re.search("^The.*Spain$", txt)

#if x:
#  print("YES! We have a match!")
#else:
#  print("No match")

#/////////////////////////////////////////////////////////////////////////////////////
#python Try...Execept
#The try block will generate an error, because x is not defined:

#x = "Hello World!"

#try:
#  print(x)
#except:
#  print("An exception occurred")

#//////////////////////////////////////////////////////////////////////////////////////
#python user input
#username = input("Enter username:")
#print("Username is: " + username)

#///////////////////////////////////////////////////////////////////////////////////////
#python string formating
#price = 49
#txt = "The price is {} dollars"
#print(txt.format(price))

#////////////////////////////////////////////////////////////////////////////////////////
#Finish python basics

#Python pip

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


