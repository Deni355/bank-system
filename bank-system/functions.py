def ShowBalance(balance):  # To show the balance
    print("\n--- Show Balance ---")
    print(f"Your current balance is: ${balance:.2f}\n")

def Deposit(balance): # To deposit money
    print("\n--- Deposit ---")
    deposit = float(input("How much do you want to deposit? $"))
    balance += deposit
    print(f"Your new balance is: ${balance:.2f}\n")
    return balance

def Withdraw(balance): # To withdraw money
    print("\n--- Withdraw ---")
    withdraw = float(input("How much do you want to withdraw? $"))
    
    if withdraw > balance: # To check if the balance is sufficient
        print("Insufficient funds!\n")
    else:
        balance -= withdraw # To withdraw the money
        print(f"Your new balance is: ${balance:.2f}\n")
        return balance

def Continue(): # To continue or exit
    print("Do you want to continue?")
    print("Type Y for yes and N for no.")
    again = input("Y/N: ")

    match again:
        case "Y" | "y":
            return True
        case "N" | "n":
            print("Thank you for using the bank system. Goodbye!")
            return False
        case _:
            print("Invalid input. Please try again.\n")