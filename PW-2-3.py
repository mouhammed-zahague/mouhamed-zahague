class Color:
    # Class attributes (constants) defined using the assignment operator (=).
    # These store special text codes (ANSI escape codes) to change the color of the output in the terminal.
    # The 'GREEN', 'RED', etc., are variable names.
    GREEN = "\033[92m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    ORANGE = "\033[38;5;208m"
    RESET = "\033[0m" # This resets the color back to the terminal's default.
    





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
        print(f"CIN:{Color.YELLOW} {self.__CIN}{Color.RESET}, Name: {Color.YELLOW}{self.__firstName}{Color.YELLOW} {self.__lastName}{Color.RESET}, Tel: {Color.YELLOW}{self.__tel}{Color.RESET}")


# Add account to client
    def add_account(self, account):
        self.__accounts.append(account)

 # Display all accounts of this client
    def listAccounts(self):
        print(f"\nAccounts of {Color.YELLOW}{self.__firstName}  {self.__lastName}{Color.RESET}:")
        if not self.__accounts:
            print(" - No accounts.")
            return
        for acc in self.__accounts:
            print(f" - Account {Color.CYAN}{acc.get_code()} {Color.RESET}| Balance = {Color.GREEN}{acc.get_balance()} DA{Color.RESET}")


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
        self.__transactions.append(f"Credit {Color.GREEN} +{amount} DA {Color.RESET}(new balance = {Color.GREEN}{self.__balance}DA{Color.RESET})")



    def debit(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        if self.__balance < amount:
            print("Insufficient balance.")
            return
        self.__balance -= amount
        self.__transactions.append(f"Debit {Color.RED} -{amount} DA {Color.RESET}(new balance = {Color.GREEN}{self.__balance}DA{Color.RESET})")
       
    
    def transfer(self, amount, target):
        if amount <= 0:
            print("Amount must be positive!")
            return
        if self.__balance < amount:
            print("Insufficient balance for transfer!")
            return
        self.__balance -= amount
        target.__balance += amount
        self.__transactions.append(f"Transfer {Color.RED}-{amount} DA{Color.RESET} to account {Color.YELLOW}{target.get_code()}{Color.RESET} (new balance = {Color.GREEN}{self.__balance}DA{Color.RESET})")
        target.__transactions.append(f"Transfer {Color.RED}+{amount} DA {Color.RESET}from account {Color.YELLOW}{self.get_code()}{Color.RESET} (new balance = {Color.GREEN}{target.get_balance()}DA{Color.RESET})")
      

    def display_Account(self):# display Accounts total
        
        print(f"Account Code:{Color.CYAN} {self.__code}{Color.RESET}, Owner: {Color.YELLOW}{self.__owner.get_firstName()} {Color.YELLOW}{self.__owner.get_lastName()}{Color.RESET}, Balance: {Color.GREEN}{self.__balance} DA{Color.RESET}")

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
        print(f"Total accounts created:    {Color.ORANGE}{Account.__nbAccounts}{Color.RESET}")
if __name__ == "__main__":
    # إنشاء عميل
    c1 = Client("123456", "Ahmed", "Benali", "0555123456")
    c2 = Client("123457", "Ahmed", "wqhqgue", "0557123456")
    c1.display_Client()
    c2.display_Client()
    # إنشاء حسابين لنفس العميل
    acc1 = Account(c1)
    acc2 = Account(c1)
    acc3 = Account(c2)
    acc1.display_Account()
    acc2.display_Account()
    acc1.credit(1000)      # إيداع 1000
    acc1.debit(200)        # سحب 200
    acc1.transfer(300, acc3)  # تحويل 300 إلى acc2
    acc1.transfer(300, acc2)
    # محاولات خاطئة لاختبار الفحص
    acc1.debit(2000)       # سحب أكثر من الرصيد
    acc1.credit(-500)      # إيداع مبلغ سلبي

   
    # عرض سجل العمليات
    acc1.displayTransactions()
    acc2.displayTransactions()
    acc3.displayTransactions()
    # عرض حسابات العميل
    c1.listAccounts()
    c2.listAccounts()

    # عدد الحسابات
    Account.displayNbAccounts()

   
   
   