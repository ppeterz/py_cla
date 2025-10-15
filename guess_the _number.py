# create a simple "guess the number" game. thecomputer will generate a random number between 1 and 20 and the user will try to get/guess it. the program will provide hint if the user number is too high, too low untill the correct number is guessed. it should also count the number of attempts.

# steps 
# use a random module " import random" 
# use if, elif, else for providing hint and chrecking the cotect  number/guess
# a ciunter to track the attempts
import random
# random.randint(min,max)
secrect_value = random.randint(1,20)
attempts = 0
print ("welcome to the guess the number game")
print("i have picked a number between 1 and 20, can you take a guess?")

while True:
    # get user input
    guess = int(input("enter your guess: "))
    attempts += 1
    #  let check the guess

    if guess < secrect_value:
        print ("your guess is too low")
    elif guess > secrect_value:
        print ("your guess is too high")
    else: 
        print (f"you guessed right {secrect_value}")
        print (f"you took {attempts} attempts")
        print ('game over')
        break
        

