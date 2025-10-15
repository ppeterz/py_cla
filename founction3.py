# default arguments: is a parameter in funtion that has an assigned value. this make parameter optional when calling the function if we dont provide a value for that parameter the default value will be used
# example
# def greet(name,pronoun="miss", message="Hi"):
#     print(f"{message}, {pronoun} {name}!")

# greet("tola")  # uses default message "hello"
# greet("How far", "Alice" , "Miss")  # overrides default message with "hi"
# example stoptime
# import time
# def count(end, start=0):
#     for x in range(start, end + 2):
#         print(x, )
#         time.sleep(1)  # pause for 1 second between numbers
#     print("Done!")
# count(5)  # counts from 0 to 5
# count(30, 15)

# keyword arguments: are arguments that are passed to a function by explicitly specifying the parameter name and its value when calling the function. this allows us to pass arguments in any order and makes the code more readable
# example   
# 255

#  Consider a function that configures a database connection using keyword argument. It might have many parameters, and using keyword arguments

# host:localhost
# port: 3000
# user: admin
# passsword: passoword
# db_name: main_db

# def connect_db(host="localhost",port= 3000, user="admin", password=2550, db_name="main_db"):
#     user_password = int(input("enter password"))
#     port_name = int(input("enter port"))

#     print(f"connecting to db_name={db_name}, on {host} {port}")
#     if password != user_password:
#         print("using custom password")
#     else:
#         print("using defUALT password")

#     if port != port_name:
#         print("using custom port")
#     else:
#         print("using default port") 
#     if password == user_password and port == port_name:
#         print("login successfully")    



# connect_db()

# lambda function: is a small anonymous function that can take any number of arguments but can only have one expression. it is often used for short, throwaway functions that are not reused elsewhere in the code
# and they primarily used for short and simple operations where a full def would be too muc, they  are often passed as agument to highr=er order functions like map, filter, and sorted

# add = lambda x, y: x+y
# print (add(10 , 5))
# is_even = lambda x: x % 3 == 0
# print(is_even(7))
# is_min = lambda a, b: a if a < b else b
# print(is_min(10, 5))

# say_hello = lambda:"hello world"
# print(f"no agument: {say_hello()}")

#   error handling with exception
# these situations offen called runtime error  and can cause the program to crash. python exception handling mechanism provides a structured way to deal with these errors and prevent the program to crash

# syntax error: these occurs when the python interpreter encounters code that does not conform to the correct syntax of the language. this can be due to misspelled keywords, missing colons, parentheses, or other syntax elements.
# if x > 5
#     print("x is greater than 5")

# runtime error: these occurs durring the execution of a program even if the syntax is correct they indicate that somting unexpected happened. 

# the try-except block is the fundament construct for handling exception in python
# try:
    # your code that might raise an exception
# except ExceptionType:
    # code to handle the exception

# example
# try:
#     num1 = int(input("enter a number "))
#     num2 = int(input("enter another number "))
#     result = num1 + num2
#     print(f"the sum is {result}")
# except ValueError:
#     print("invalid input. please enter a valid number.")
# except ZeroDivisionError:
#     print("error: division by zero is not allowed.")

#  haandling multiple exceptions
# try:
#     value = int(input("enter some value: "))
#     print(5//value)
# except (ValueError, ZeroDivisionError):
#     print("invalid input. or division by ero occurred")

# try:
#     my_list = [1,2,3]
#     index = int(input("enter an index: "))
#     print(my_list[index])
# except ValueError:
#     print("please enter a valid number")
# except IndexError:
#     print("index out of range")
# except Exception as e: # catching a generic exception as a last resort
#     print(f"an error occurred: {e}")

# the exception as e syntax allows us to capture the exception object and access its message or other attributes for more detailed error reporting.

# the else block can  be included affer all except blocks. the code inside the else  is executed if  thy try block completes without raising any exceptions.

try:
    file_name = input("enter file name: ")
    with open (file_name, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print(f"file {file_name} not found")
else:
    print ("file read successfully")
    print(content[:50] + "..." if len(content) > 50 else content)


# assignment
# Project Goal:
# Create a command-line application that simulates basic ATM operations: checking balance, depositing money, and withdrawing money. The simulator should be robust enough to handle invalid user inputs gracefully using exception handling.

# Required Features:
# Initial Balance: Start with a predefined initial balance (e.g., 1000).
# Display Balance: A function to show the current account balance.
# Deposit: A function to add funds to the account.
# Must handle non-numeric input for the deposit amount.
# Must handle negative or zero deposit amounts.
# Withdraw: A function to remove funds from the account.
# Must handle non-numeric input for the withdrawal amount.
# Must handle negative or zero withdrawal amounts.
# Must prevent withdrawal if insufficient funds are available.
# Main Menu Loop: Present options to the user (deposit, withdraw, check balance, exit) and continuously process their choices until they choose to exit.

# Error Handling: Implement try-except blocks to catch ValueError for invalid numeric inputs and other logical errors (like insufficient funds).