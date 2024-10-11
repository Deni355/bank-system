from functions import ShowBalance, Deposit, Withdraw, Continue
from accounts import CheckAccount

is_running = True # To keep the program running

print("\n--- Bank System ---")
print("Welcome to the bank system!")

balance = CheckAccount() # To set the balance of the account

while is_running:
    print("--- Options ---")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    option = int(input("Choose an option: ")) # To choose an option

    match option:
        case 1:
            ShowBalance(balance)
            is_running = Continue() # To continue or exit
        case 2:
            balance = Deposit(balance)
            is_running = Continue()
        case 3:
            balance = Withdraw(balance)
            is_running = Continue()
        case 4:
            is_running = False
            print("Thank you for using the bank system. Goodbye!")
        case _:
            print("Invalid input. Please try again.\n")