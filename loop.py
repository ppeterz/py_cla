# loops are fundamental control sttuctures that allows a block of code  to be executed repeatedly. this is essential for automating repetitive tasks, processing collections of data and performing operations until a certain codition is met.
# types of loops in python
# for loop  
# while loop
# the break and continue statement

# syntax

# for item in sequence:

#  the For loop is used for iterating over a squence (such as a list, tuple, strings and range) or other iterable objects.
 
#  looping over a list
# fruits = ['apple', 'banana', 'cherry']

# for fruits in fruits:
#     print(f'i like {fruits}')

# # looping over a string
# word = "python"
# for char in word:
#     print(char)

# the range() function
# the range function is ofthen used with for loops to generate a sequence of numbers. its a very memory efficient way to create numerical sequences

# for p in range(10):
#      print(p)
# for i in range(2,7):
#     print(i)

# for j in range(1,10,4,):
#     print(j)  

# the while loop
# the while loop repeatedly executes a block of code as long as a specificied condition remains True. it is used when you dont know in advance how many times the loop needs to run, but  rather needs to continue based on a condition

# while condition:

# example: simple countdown
# countdown = 20

# while countdown > 0:
#     print(countdown)
#     countdown -= 1  
# print("blast off!")

# example: user input validation
# password = ""

# while password != "peter":
#     password = input("enter the password: ")
#     if password != "peter":
#         print("incorrect password, try again")
# print("access granted")

# classwork
# write a program that will ask a user to enter a number and print all the even numbers from 1 to that number using for loop and while loop.

# user_number = int(input("enter a number: "))

# print('even numbers using for loop')

# for i in range(2, user_number + 1, 2):
#     print(i, end = ' , ')

# print('\neven numbers using while loop')

# i =2
# while i <= user_number:
#     print(i, end = ' , ')
#     i += 2


# nested loops:
# it is just like conditional statements, loops can also be nested. it occur when one loop is placed inside another loop. the inner loop completes all its iterations for each single iterations for each single iteration of the outer loop

# example: multiplication table
# print('multiplication table (1-3): ')

# for i in range (1,6): # outter loop
#     for j in range (1,5): # inner loop for columns
#         print(f"{i}+{j}= {i+j}\t", end=" ") # \t tab spacing
#     print() # Newline after each row for the inner loop

# for i in range (1 , 10):
#     for j in range (i):
#         print ("*", end = " ")
#     print ()

# example: look throuht an item

for i in range (1,5):   
    for x in range (1,5):
        print(f"{i} and {x}\t", end=' ')
    print()

# controlling loops": it provides  special statemet (break and continue) oit gives you more control over how loops behave during execution, it is used when an exit condtion is met inside the loop, and there's no need to continue with any further iteration
# example: searching for an item/ looping through an item

name = ["bola", "tope", "tola", "josh", "jane", "peter"]
search_value = "tobi"
found = False

for num in name:
    if num == search_value:
        print(f"{search_value} found!")
        found = True
        break # exit the code as soon as it is found
print(f"checking {num}...")

if not found:
    print(f"{search_value} not found in the list.")

# the continue statement: the continue statement skips the rest of the current iteration of the loop and moves on to the next iteration. the loop dose not terminate: it just bypass the remaining code  within the current loop block for that specific iteration 

# example: skipping even numbers
# for i in range (1, 20):
#     if i % 5 == 0: # it skips to the odd number
#         continue # skips to the next number
#     print(f"{i} is an even number")


# when i is 2, i % 2 == 0 is true, continue to execute the code and the it print the odd number while it skipper for i=2 the loop then proceeds to i=3

# loop patterns: accumulators:used to sum or buil a total from a series of values/numbers

# total = 0
# numbers = [1,2,3,4,5,6]

# for num in numbers:
#     total += num # add each number total
# print(f" sum: {total}")

# atm pin verification

my_pin = "7890"
attepmts = 0

while True:
    pin = input("enter your 4 digit pin: ")
    attepmts += 1

    if pin == my_pin:
        print ('access granted')
        break
    else:
        print (' Wrong pin')
        print (attepmts)

    if attepmts == 3:
        print ('card blocked after 3 attempts')
        break

#  classwork
# ATM machine simulation using only loops and conditional statement. take user input 
# 1, check the pin verification
# 2, check account balance
# 3, deposit money
# 4, withdraw money
# 5, exit  