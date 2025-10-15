# getting data out of a function

# we need a function to calculate a value and give it back to us so we can use it elsewhere in our code.
# this done by using the keyword "return"
#  the return value is the value that a function sends back to the part of the code that callled it, this value can be store in a varible or used directly in another expression
# 
# example
# def add_number(num1,num2):
#     total = num1 + num2
#     return total

# sum_total = add_number(5,23) 
# print(sum_total)

# # we can call the return value
# double_sum = sum_total * 2
# print(double_sum)

# explame
# def diff_number(a,b):
#     result = a - b
#     return result
# diff_result = diff_number(20,5)
# print (diff_result)

# def sum_number(a):
#     result1 = a + diff_result
#     return result1
# sum = sum_number(10)
# print (sum)
reading = float(input("enter your reading: "))
sensor_reading = 89
sensor_value = 54
call = 6.3
def temp_value (temp):
    sensor_value1 = 54
    cal = temp + reading
    return cal
temp_result = temp_value (2.5)
print (temp_result)

def temp_state ():
    call + sensor_reading
    if temp_result <= sensor_reading:
        print ("cold")
    else:
        print ("hot")
temp_state()


# unit converter
# create a function that convert celsius to fahrenheit the  F = (C × 9/5) + 32 and also another function for fahrenheit to celsius c = (f - 32) * 5/9
# kilometer to miles and miles to kilometer km = miles* 0.62137119, miles = km / 0.62137119