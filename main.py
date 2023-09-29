#Author: Francis Nguyen
#Date: 10/28/2022
#Purpose: Users will be able to create a checking and savings account
#         and will be able to deposit, withdraw, and view their account information
#         using a menu interface.

from bank import Checking, Savings

'''
    Function Name: prompt
    Purpose: Manages newly created checking/savings accounts and
             validates the balance using the validate() function.
    Return Value: account's name and balance as a tuple
'''
def prompt():
    name = str(input("Enter owner's name: "))
    while True:
        try:
            balance = float(input("Enter initial balance: "))
            if balance < 0:
                balance = validate()
        except:
            print("Invalid input: an float value was expected. Try again: ")
            balance = validate()
        
        break

    return (name,balance)

'''
    Function Name: validate
    Parameter: number - optional parameter defaulted to 0; carries over
               each recursion if value error is found.
    Purpose: Repeatedly prompts for number until a valid float value is received
    Return Value: Returns the validated float value
'''
def validate(number=0):
    try:
        number = float(input("Enter a greater than or equal to zero: "))
        while number < 0:
            number = float(input(''))
        return number
    except:
        print("Invalid input: an float value was expected. Try again: ")
        validate(number)

'''
    Function Name: checkAccount
    Parameter: accountList - list of accounts from the main script,
               which is used to find existing account numbers from the list
    Purpose: Check to see if user's account number matches with an existing one
    Return Value: Returns either the account number's object or a False value,
                  which tells the main script to exit out of deposit/withdraw
                  branch
'''
def checkAccount(accountList):
    isValid = False
    print("Enter account number:")
    while True:
        try:
            accountNumber = int(input(''))
            #For each object in the list, check to see if account numbers match
            for obj in accountList:
                if accountNumber == obj.getAccountNumber():
                    isValid = True
                    return obj

            if isValid != True:
                print("That account number does not exist")
                return False
            
        except ValueError:
            print("Invalid input: an integer value was expected. Try again: ")
            continue
            
#Main Script
if __name__ == "__main__":
    
    #Create a single List for BankAccount objects
    accountList = []
    
    while True:
        
        print("1. Create Savings Account\n\
2. Create Checking Account\n\
3. Deposit\n\
4. Withdraw\n\
5. Perform End of Month Operations\n\
6. Display Savings Accounts\n\
7. Display Checking Accounts\n\
8. Display All Accounts\n\
9. Exit")
        
        #Input validation (only accept ints from 0 to 9)
        try:
            answer = int(input("Enter your choice: "))
            if answer <= 0 or answer > 9:
                print("Invalid choice. Try again.\n")
                continue
        except:
            print("Invalid choice. Try again.\n")
            continue
        
        #Create a Savings account
        if answer == 1:
            print("Savings Account")
            name, balance = prompt()
            savingsAccount = Savings(name, balance)
            accountList.append(savingsAccount)
            print("Account added\n")
            
        #Create a Checking account
        if answer == 2:
            print("Checking Account")
            name, balance = prompt()
            checkingAccount = Checking(name, balance)
            accountList.append(checkingAccount)
            print("Account added\n")
        
        #Deposit
        if answer == 3:
            print("Deposit")
            account = checkAccount(accountList)
            if account == False:
                continue
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount < 0:
                    amount = validate()
            except:
                print("Invalid input: an float value was expected. Try again: ")
                amount = validate()

            account.deposit(amount)
            print("\n")
                        
        #Withdraw
        if answer == 4:
            print("Withdraw")
            account = checkAccount(accountList)
            if account == False:
                continue
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount < 0:
                    amount = validate()
            except:
                print("Invalid input: an float value was expected. Try again: ")
                amount = validate()
                    
            if account.getBalance() - amount < 0:
                print("You do not have enough funds \n")
                continue

            account.withdraw(amount)
            print("\n")
        
        #Perform End of Month Operations
        if answer == 5:
            for index in accountList:
                index.endOfMonth()
            print("End of month operations have been performed\n")
        
        #Display Savings Accounts
        if answer == 6:
            for index in accountList:
                if isinstance(index, Savings):
                    print(index)
        
        #Display Checking Accounts
        if answer == 7:
            for index in accountList:
                if isinstance(index, Checking):
                    print(index)
        
        #Display All Accounts
        if answer == 8:
            for index in accountList:
                print(index)
        
        if answer == 9:
            break
        
    #Goodbye message!
    print("Good-bye!")
