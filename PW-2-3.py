# Class Client
class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.__accounts = []

    # Getters and setters for all attributes
    def get_CIN(self): return self.__CIN
    def get_firstName(self): return self.__firstName
    def get_lastName(self): return self.__lastName
    def get_tel(self): return self.__tel
    def get_accounts(self): return self.__accounts   


    def set_tel(self, tel): self.__tel = tel

    def display_Client(self):
        print(f"CIN: {self.__CIN}, Name: {self.__firstName} {self.__lastName}, Tel: {self.__tel}")


# Add account to client
    def add_account(self, account):
        self.__accounts.append(account)

 # Display all accounts of this client
    def listAccounts(self):
        print(f"\nAccounts of {self.__firstName} {self.__lastName}:")
        if not self.__accounts:
            print(" - No accounts.")
            return
        for acc in self.__accounts:
            print(f" - Account {acc.get_code()} | Balance = {acc.get_balance()} DA")


# Class Account
class Account:
    __nbAccounts = 0  # static variable for sequential codes

    def __init__(self, owner):
        Account.__nbAccounts += 1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = owner
        self.__transactions = []


        owner.add_account(self)

    # Access methods
    def get_code(self): return self.__code
    def get_balance(self): return self.__balance
    def get_owner(self): return self.__owner

    # Credit and debit methods
    def credit(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        self.__balance += amount
        self.__transactions.append(f"Credit + {amount} DA (new balance = {self.__balance})")



    def debit(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        if self.__balance < amount:
            print("Insufficient balance.")
            return
        self.__balance -= amount
        self.__transactions.append(f"Debit - {amount} DA (new balance = {self.__balance})")
       
    
    def transfer(self, amount, target):
        if amount <= 0:
            print("Amount must be positive!")
            return
        if self.__balance < amount:
            print("Insufficient balance for transfer!")
            return
        self.__balance -= amount
        target.__balance += amount
        self.__transactions.append(f"Transfer -{amount} DA to account {target.get_code()} (new balance = {self.__balance})")
        target.__transactions.append(f"Transfer +{amount} DA from account {self.get_code()} (new balance = {target.get_balance()})")
      

    def display_Account(self):# display Accounts total
        
        print(f"Account Code: {self.__code}, Owner: {self.__owner.get_firstName()} {self.__owner.get_lastName()}, Balance: {self.__balance} DA")

     # Display history
    def displayTransactions(self):
        print(f"\nTransaction History for account {self.__code}:")
        if not self.__transactions:
            print(" - No transactions yet.")
            return
        for t in self.__transactions:
            print(" -", t)



    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)
   