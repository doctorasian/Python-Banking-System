#Author: Francis Nguyen
#Date: 10/28/2022
#Purpose: This file houses the BankAccount, Checking, and Savings classes.
#         Checking and Savings classes inherit BankAccount methods and attributes.


from abc import abstractmethod, ABC

class BankAccount(ABC):
    #Account number generation begins from 1000
    __nextAccountNumber = 1000
    
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance
        self.__accountNumber = BankAccount.__nextAccountNumber
        #when a new bank account is instantiated,
        #increment the acc. number for a future account
        BankAccount.__nextAccountNumber += 1
    
    @staticmethod
    def getNextAccountNumber():
        return BankAccount.__nextAccountNumber
    
    @abstractmethod
    def endOfMonth(self):
        pass
    
    #Getters/Setters
    def getOwner(self):
        return str(self.__owner)
    
    def getBalance(self):
        return float(self.__balance)
    
    def getAccountNumber(self):
        return int(self.__accountNumber)
    
    #Deposit/Withdraw Methods
    def deposit(self, amount):
        self.__balance += amount
        #Note: amount is a float value
    def withdraw(self, amount):
        self.__balance -= amount

    #Output
    def __str__(self):
        res = 'Account Number: ' + str(self.getAccountNumber()) + '\n'
        res += 'Account Owner: ' + str(self.getOwner()) + '\n'
        res += 'Account Balance: ' + f'${self.getBalance():.2f}' + '\n'
        return res
    

class Savings(BankAccount):
    
    def __init__(self, owner, balance=0, interestRate = 3.25):
        BankAccount.__init__(self, owner, balance)
        self.__interestRate = interestRate
        
    def getInterestRate(self):
        return float(self.__interestRate)
    
    def setInterestRate(self, value):
        self.__interestRate = value
    
    def __str__(self):
        res = BankAccount.__str__(self)
        res += 'Annual Interest Rate: ' + f'{self.getInterestRate():.2f}%'
        return res
    
    def endOfMonth(self):
        monthlyInterestRate = self.__interestRate/12
        interestEarned = self.getBalance() * monthlyInterestRate * (1/100)
        self.deposit(interestEarned)
    
class Checking(BankAccount):
    
    def __init__(self, owner, balance=0):
        BankAccount.__init__(self, owner, balance)
        self.__transactions = 0
    
    def getTransactionsNum(self):
        return int(self.__transactions)
    
    #Update transactions everytime deposit/withdraw is made
    def deposit(self, amount):
        BankAccount.deposit(self, amount)
        self.__transactions += 1
    
    def withdraw(self, amount):
        BankAccount.withdraw(self, amount)
        self.__transactions += 1
    
    def __str__(self):
        res = BankAccount.__str__(self)
        res += 'Transactions this month: ' + str(self.getTransactionsNum())
        return res
    
    #If transactions exceed 7, charge 5.00 and reset transactions to 0
    def endOfMonth(self):
        if self.__transactions > 7:
            self.withdraw(5.00)
        self.__transactions = 0

