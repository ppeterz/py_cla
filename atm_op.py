# ATM Simulator
account_balance = 1000.00  # Initial balance

def display_balance():
   
    print(f"\n💰 Your current balance is: ₦{account_balance:.2f}")

def deposit():
   
    global account_balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("⚠️ Deposit amount must be greater than zero.")
            return
        account_balance += amount
        print(f"✅ Successfully deposited ₦{amount:.2f}. New balance: ₦{account_balance:.2f}")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric amount.")

def withdraw():
    
    global account_balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("⚠️ Withdrawal amount must be greater than zero.")
            return
        if amount > account_balance:
            print("❌ Insufficient funds. Transaction cancelled.")
            return
        account_balance -= amount
        print(f"✅ Successfully withdrew ₦{amount:.2f}. New balance: ₦{account_balance:.2f}")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric amount.")

def main_atm_program():
   
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            display_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("\nThank you for using the ATM. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

# # Run the program
# if __name__ == "__main__":
#     main_atm_program()
main_atm_program()