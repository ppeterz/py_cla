# functions are reusable block of code that can perform a specific task.

# function name: the you give to the code Block
# function body: the set of instruction inside the function
# function calling: the act of calling or running the code inside anther scope

# def word: this signals the start of a function definition
#  def  my_function the function name

def my_function():
    print("-------------")
    print("hello world")
    print("=============")
    print(10*10)

# function calling
print("befora calling function")
my_function()
print ("end of function calling")

# parameters and arguments
# a parameter is a special variable the you list inside the bracket () in the function def. it act as a placeholder for a value that you will provide when you call the function
# argument is the actual value that you pass to the function when you call it.

def greet_person(name):
    print("-------------")
    print(f"hello {name}")
    print("=============")
 
greet_person("tope")

# multiple parameters
def show_workings(name,amount):
    print(f"user: {name}")
    print(f"amount: {amount}")

show_workings("peter", 5000)

# classwork
# write a function called calculator() taht takes two numbers and print their
# sum, difference, product and quotient.
# call the function with  25 and 20

def calculator(a,b):
    print(f"sum: {a+b}")
    print(f"difference: {a-b}")
    print(f"product: {a*b}")
    print(f"quotient: {a/b}")

calculator(25,20)

# # classwork
# write a function called calculate_grade() that takes a student score as input and prints their grade based on the following grading scale:
# #"A" if score >= 70
# #"B" if score >= 60
# #"C" if score >= 50
# #"D" if score >= 40
# #"F" if score < 40
# call the function with three different scores

score = int(input("enter your score: "))
def calculate_grade(score):
    if score >= 70:
        print("A")
    elif score >= 60:
        print("B")
    elif score >= 50:
        print("C")
    elif score >= 40:
        print("D")
    else:
        print("F")
print(f"your grade is: {score}")
calculate_grade(score)


