# if statement is a conditional statement that runs a block of code if a specified condition is true
# if else statement is a conditional statement that runs a block of code if a specified condition is true and another block of code if the condition is false
# elif statement is a conditional statement that runs a block of code if a specified condition is true

# if_statement = True
# if if_statement:
#     print("if statement is true")
# else:
#     print("if statement is false")
    
# passmark = 30
# totalmark = 60
# student_score = int(input("enter your score: "))
# if student_score >= passmark and student_score <= totalmark:
#     print("you have passed")
# else:
#     print("you have failed")

# classwork
# create a program that will check if a user is eligible to vote
# the program should ask the user to enter their name and age 
# print a message that will tell the user if they are eligible to vote or not with their name and age

# votingAge = 18

# name = input("enter your name: ")
# age = int(input("enter your age: "))
# if age >= votingAge:
#     print (f"{name} is {age}, you are eligible to vote.")
# else:
#     print (f"{name} is {age}, you are not eligible to vote.")
    
# assignment
# write a program that check if level of temprature and humidity is high or low, ask user for both value and print the state of the weather if its cold, hot and humidy.  

# temp = int(input("enter the temprature: "))
# humidity = int(input("enter the humidity: "))

# if temp >=30 and humidity >= 70:
#     print("the weather is hot and humid")
# else:
#     print("the weather is cold and dry")

# nested if statement/condtional statement
# nested conditions occour when one if/elif/else statement is placed insideanother if/elif/else block. this allows  for more granular/complex decision making processes, where a scondry condition depends on the outcome of a primary decision.

# example: a movie theater might have different ticket prices based on age and then further conditions are needed.

# age = int(input('Enter your age '))
# day = input("enter the day (weekdays/weekend) ").lower()

# ticket_price = 0

# if age < 12:
#     if day == 'weekday':
#         ticket_price = 1000
#     elif day == 'weekend':
#         ticket_price = 1500
#     else:
#         print("Invalid day entered")
# elif age >= 12 and age < 65:
#     if day == 'weekday':
#         ticket_price = 2000
#     elif day == "weekend":
#         ticket_price = 2500
#     else:
#         print("Invalid day entered")
# elif age >= 65 and age < 120:
#     if day == 'weekday': 
#         ticket_price = 3000
#     elif day == "weekend":
#         ticket_price = 3500
#     else:
#         print("Invalid day entered")
# else:
#     print('invalid age')

# if ticket_price > 0:
#     print(f"your ticket price is: #{ticket_price}")

# # classwork
# create a python program that prompts the user to enter a numerical score (0-100) and then displays the corresponding letter grade (A, B, C, D, F) based on the predefined grading scale:
# 90-100: A
# 80-89: B  
# 70-79: C
# 60-69: D  \
# 0-59: F

# student_score = int(input("enter your score: "))
# test= int(input("enter your test score: "))

# if student_score > 100 or student_score < 0:
#     print("invalid score")
# elif student_score >= 90:
#     if student_score < test:
#         print (f'your score {student_score} is less than test score {test}')
#     else:
#        print (f'your score {student_score} is greater than test score {test}')  
#     grade = 'A'
# elif student_score >= 80:
#     grade = 'B'
# elif student_score >= 70:   
#     grade = 'C'
# elif student_score >= 60:   
#     grade = 'D'             
# else:
#     grade = 'F'     

# print(f"your grade is: {grade}")

# assignment nested if statement
# create a program that will check if a user is eligible to vote and if they are eligible, check if they are registered to vote
# the program should ask the user to enter their name, age and if they are registered to vote (yes/no)
# print a message that will tell the user if they are eligible to vote or not with their name, age and registration status

name = input("enter your name:  ")
age = int(input("enter your age: "))
reg_state = input(' are registed true/false ')
max_age = 100
if_registed = True
voting_age = 18

if age < voting_age:
    print('you are not eligible')
elif age >= voting_age:
    if reg_state == "true":
        print(f'{name} your are {age} years old and you are eligible to vote, registration status {reg_state}')
    elif reg_state == "false":
        print(f'{name} your are {age} years old and you are not eligible to vote, registration status {reg_state}')
    else:
        print('invalid registration status')
elif age > max_age:
    print('invalid age')
        

