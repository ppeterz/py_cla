# default arguments: is a parameter in funtion that has an assigned value. this make parameter optional when calling the function if we dont provide a value for that parameter the default value will be used
# example
# def greet(name,pronoun="miss", message="Hi"):
#     print(f"{message}, {pronoun} {name}!")

# greet("tola")  # uses default message "hello"
# greet("How far", "Alice" , "Miss")  # overrides default message with "hi"
# example stoptime
import time
def count(end, start=0):
    for x in range(start, end + 2):
        print(x, end=" ")
        time.sleep(1)  # pause for 1 second between numbers
    print("Done!")
count(5)  # counts from 0 to 5
count(30, 15)        
