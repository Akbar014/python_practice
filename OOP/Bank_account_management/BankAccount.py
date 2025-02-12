import random

class BankAccount:
    account_number = random.random()
    holders_name = ""
    balance = 0
    def __init__(self, holders_name, balance):
        self.holders_name = holders_name
        self.balance = 0

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Current balance : {self.balance}")


    def get_account_details(self):
        print(f"Account Noo: {self.account_number}, Account owner : {self.holders_name} , Account balance: {self.balance}")



obj = BankAccount("akbar", 20000)
obj.deposit_money(2000)
obj.display_balance()
obj.get_account_details()






class BankAccount:
    # Class variable to keep track of the next account number
    next_account_number = 1000

    def __init__(self, account_holder_name):
        """
        Constructor to initialize the account details.
        """
        self.account_holder_name = account_holder_name
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1  # Increment account number for the next account
        self.__balance = 0  # Private attribute to store the balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """
        Method to display the current balance.
        """
        print(f"Account {self.account_number} balance: ${self.__balance}")

    def __str__(self):
        """
        String representation of the account.
        """
        return f"Account Number: {self.account_number}, Holder: {self.account_holder_name}, Balance: ${self.__balance}"

 
# Example Usage
if __name__ == "__main__":
    # Create two bank accounts
    account1 = BankAccount("Alice")
    account2 = BankAccount("Bob")

    # Perform operations on account1
    print(account1)
    account1.deposit(500)
    account1.withdraw(200)
    account1.get_balance()

    # Perform operations on account2
    print(account2)
    account2.deposit(1000)
    account2.withdraw(1500)  # Attempt to withdraw more than the balance
    account2.get_balance()



