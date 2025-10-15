# what is variables: variables are container that holds values e.g age_variable = value it is use to store differebt kind of information or data type e.g int, float, str, bool

# variable_name = value 
# variableName = value
# variable_name_house = value 

# 1st_name = value # invalid
# first-name = value # invalid

# firstname = value
# firstNmae = value

# first_name = "bola"

# Data types in python
# int which hold whole number e.g 5, 10, -20
# float which hold decimal number e.g 5.6, 10.2, -20
# bool which hold true or false e.g True, False
# str which holds strings "tola" "5225" "True"

# int wifi_password = 5;
#  type converstion in python to check the varibale type and to convert from one variblae to another, anyn input for a user python will always read a strings.

# firstName = "jane doe"
# age = 20
# height = 5.6
# is_student =  True

# print (type(firstName))
# print (type(age))
# print (type(height))
# print (type(is_student))

# getting user input
# the input function is use to get input from a user, and it is always seen as strings even if the user type a number 5, 10, 20. this is where the type converstion becomes essential.

# the Syntax/ or how it is been called
# username = input("Enter your username: ")
# user_password = input("Enter your password: ") 

# print ("your username is :" + username)
# print ("your password is :" + user_password)

# name = "jane doe"

# print ("Welcome: " + name + " home")

# type conversion 
#  int(value) this convert the value to an integer
#  float(value) this convert the value to a float
#  str(value) this convert the value to a string

#   strings to integer
# actual_value = 10
# new_coverstion = str(actual_value)  # the syntax for to convert from strings to int 
# print (f"the actual_value is  {actual_value} and is of type {type(actual_value)}")
# print (f"the new_coverstion is  {new_coverstion} and is of typs {type(new_coverstion)}")
# "f" it is a way to format string in python

# ass
# create two input for a user and convert them to integer 

# x = input("enter x value")
# y = input("enter y value")

# x_int = int(x)
# y_int = int(y)

# print (x_int + y_int)

# Arithmetic operations in python
# + addition
# - subtraction     
# * multiplication
# / division
# % modulus (remainder)
# ** exponentiation (power)
# // floor division (quotient without the decimal part)
# order of operation (BODMAS) bracket, order, division, multiplication, addition, subtraction
# num_1 = 10
# num_2 = 18

# print (f"{num_1} + {num_2} = {num_1 + num_2}")
# #print (num_1, "+", num_2, "=", num_1 + num_2 )
# print (f"{num_1} - {num_2} = {num_1 - num_2}")

# order of operation : python follows the  standard mathematical order of operation (BODMAS) bracket, order, division, multiplication, addition, subtraction
# the division from left to right, addition and subtraction from left to the right

# result = 10 + 5 * 2
# print (result) 

# result_bracket= (10 +50) * 5 
# print (result_bracket)

# long_bracket = 2+5 * 10 // 2 - (5 + 2) * 3
# print (long_bracket)

# classwork:
# create a simple calculator that takes two numbers from a user and perform all the arithmetic operations
# addition, subtraction, multiplication, division, modulus, exponentiation, floor division

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

# print (f"{num1} + {num2} = {num1 + num2 / num2 * (num1*num2)}")
print (f"{num1 + num2 / num2 * (num1*num2) - num1 // num2 % num1}")
print ( 10 + 5 /  5 * (10*5) - 10 // 5 % 10)
