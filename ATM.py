pin = "5566"
balance = 5000
attempts = 0

while attempts < 3:
    enter_pin = input("enter your pin")
    if enter_pin == pin:
        print("login successful\n")
        break
    else:
        attempts += 1
        print("Wrong pin. try again")
if attempts == 3:
    print("card blocked, 3 wrong attempts")
else:
    while True:
        print("1. check balance")
        print("2. deposit money")
        print("3. withdraw money")
        print("4. exit")
        choice = input("enter your choice")
        if choice == "1":
            print(f"your balance is {balance}")
        elif choice == "2":
            deposit = int(input("enter deposit amount: "))
            if deposit > 0:
             balance += deposit
             print(f"your new balance is {balance}")
             print("deposit successful")
            else: 
                print("invalid deposit amount")
        elif choice == "3":
            withdraw = int(input("enter withdraw amount: "))
            if withdraw > 0 and withdraw <= balance:
                balance -= withdraw
                print(f"your new balance is {balance}")
            else:
                print("invalid withdraw amount")
        elif choice == "4":
            print("Thanks for banking with us ")
            break
        else:
            print("invalid choice")

print (enter_pin)