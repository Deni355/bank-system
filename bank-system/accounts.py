import pandas as pd

Accounts = { # To create a DataFrame
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Money': [5000, 6000, 7000, 8000]
}

df = pd.DataFrame(Accounts) # To create a DataFrame

def CheckAccount(): # To set the balance of the account
    name = input("Enter your name: ")
    if name not in df['Name'].values:
        print("Account not found!\n")
        print("Do you want to create a new account?")
        newacc = input("Y/N: ")
        match newacc:
            case "Y" | "y": #To create a new account with a balance of 0
                newAccounts(name, 0)
                balance = 0
                return balance
            case "N" | "n":
                print("Thank you for using the bank system. Goodbye!")
                return 0
    else:
        print(f"Welcome, {name}!\n")
        balance = df.loc[df['Name'] == name, 'Money'].values[0] #To get the balance of the account
        return balance

def newAccounts(name, balance):
    df.loc[len(df.index)] = [name, balance] #To add a new row
    print(f"Account created for {name} with a balance of ${balance:.2f}\n")