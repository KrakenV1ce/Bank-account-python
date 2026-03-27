class BankAccount():
    def __init__(self, titular, balance, login, password):
        self.titular = titular
        self.balance = balance
        self.historic = []
        self.historic_rec = []
        self.login = login
        self.password = password
        self.error = 3
        self.locked = False

    def Deposit(self, mount):
        if mount > 4000:
            print("U can't Deposit that much")
            return
        elif mount <= 0:
            print("Error Negative Value")
            return
        self.balance += mount
        self.historic.append("Deposit +" + str(mount) + " Balance : " + str(self.balance))

    def Withdraw(self, mount):
        if mount > 600:
            print("U can't Withdraw that much")
            return
        elif mount <= 0:
            print("Error Negative Value")
            return
        elif mount > self.balance:
            print("Inssufisant Money")
            return
        self.balance -= mount
        self.historic.append("Withdraw -" + str(mount) + " Balance : " + str(self.balance))

    def Transfer(self, mount, receiver_choose):
        if mount > 2000:
            print("U can't Transfer that much")
            return
        elif mount <= 0:
            print("Error Negative Value")
            return
        elif mount > self.balance:
            print("Inssufisant Money")
            return
        self.balance -= mount
        receiver_choose.balance += mount
        self.historic.append("Transfer to " + receiver_choose.titular + str(mount) + " Balance : " + str(self.balance))
        receiver_choose.historic_rec.append("Transfer from " + self.titular + " +" + str(mount) + " Balance : " + str(receiver_choose.balance))

    def Back(self):
        r = str(input("if return, write 'back' : ")).lower()
        if r == 'back':
            pass

    def display_Account(self):
        print("Account of : ", self.titular)

    def display_Balance(self):
        print("Amount : ", self.balance)

    def display_Menu(self):
        print("=== Welcome To AppBank ===")
        print("1- Watch Account Name")
        print("2- Watch Balance")
        print("3- Make a Deposit")
        print("4- Make a Withdraw")
        print("5- Show to History")
        print("6- Transfer Money")
        print("7- Show Transfer History")
        print("8- Leave")

    def display_Historic(self):
        if not self.historic:
            print("Not Historic Yet")
        for element in self.historic:
            print(element)

    def display_Historic_Receiver(self):
        if not self.historic_rec:
            print("Not Transfer Histoic Yet")
        for elmnt in self.historic_rec:
            print(elmnt)

    def User_Log(self, Login):
        return Login == self.login
    
    def User_Pass(self, Password):
        if self.error <= 0:
            self.locked = True

        if self.locked:
            print("Account Blocked !!")
            return False
        elif Password == self.password:
            print("successfully password")
            return True
        
        if Password != self.password:
            self.error -= 1
            return
        
def Loging(accounts, accnts):
    for account in accounts:
        if account.User_Log(accnts):
            return account
    return False

def Contact(accounts, account_found):
    receiver_possible = []
    for account in accounts:
        if account != account_found:
            receiver_possible.append(account)

    for i, account in enumerate(receiver_possible):
        print(i +1, "-", account.titular)
        
    try:    
        choice = int(input("Choose Contact : "))
    except:
        print("Invalid Syntax !!")

    if 1 <= choice <= len(receiver_possible):
        return receiver_possible[choice - 1]
    else:
        print("Invalid Syntax !!")
        return False

def Save_Accounts(accounts):
    with open("accounts.txt", "w", encoding="utf-8") as file:
        for account in accounts:
            line = (account.titular + "|"
                    + str(account.balance) + "|"
                    + account.login + "|"
                    + account.password + "|"
                    + str(account.error) + "|"
                    + str(account.locked) + "\n"
                    )
            file.write(line)
                    
def Load_Accounts():
    
    accounts = []

    try:
        with open("accounts.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                titular = parts[0]
                balance = float(parts[1])
                login = parts[2]
                password = parts[3]
                error = int(parts[4])
                locked = parts[5] == "True"

                account = BankAccount(titular, balance, login, password)
                account.error = error
                account.locked = locked

                accounts.append(account)
    except FileNotFoundError:
        accounts = [
            BankAccount("Joe", 2000, "Joedavid@gm.com", "J03Davidson"),
            BankAccount("Marry", 3000, "MarryChrist@gm.com", "ChristM4d"),
            BankAccount("Tony", 6000, "TonyStar@gm.com", "ImOnlyCyborg"),
            BankAccount("Mich", 8000, "Michelangelo@gm.com", "M1chng3l0")
            ]
        Save_Accounts(accounts)
    return accounts
        
C = BankAccount("Joe", 2000, "Joedavid@gm.com", "J03Davidson")
C1 = BankAccount("Marry", 3000, "MarryChrist@gm.com", "ChristM4d")
C2 = BankAccount("Tony", 6000, "TonyStar@gm.com", "ImOnlyCyborg")
C3 = BankAccount("Mich", 8000, "Michelangelo@gm.com", "M1chng3l0")

accounts = Load_Accounts()

while True:
    e = str(input("Enter ID : "))
    f = str(input("Enter Password : "))
    account_found = Loging(accounts, e)
    if account_found:
        if account_found.User_Pass(f):
            while True:
                account_found.display_Menu()
                try:
                    Choice = int(input("Choose Option Number : "))
                except:
                    print("Please enter a correct Option Number")
                    continue
                if Choice == 1:
                    account_found.display_Account()
                    account_found.Back()
                elif Choice == 2:
                    account_found.display_Balance()
                    account_found.Back()
                elif Choice == 3:
                    a = float(input("Insert a Value : "))
                    a1 = str(input("Confirm ? (yes/no) : ")).lower()
                    if a1 == 'yes':
                        account_found.Deposit(a)
                        Save_Accounts(accounts)
                        account_found.Back()
                    elif a1 == 'no':
                        account_found.Back()
                elif Choice == 4:
                    b = float(input("Insert a Value : "))
                    b1 = str(input("Confirm ? (yes/no) : ")).lower()
                    if b1 == 'yes':
                        account_found.Withdraw(b)
                        Save_Accounts(accounts)
                        account_found.Back()
                    elif b1 == 'no':
                        account_found.Back()
                elif Choice == 5:
                    account_found.display_Historic()
                    account_found.Back()
                elif Choice == 6:
                    d = float(input("Insert a Value : "))
                    d1 = str(input("Confirm ? (yes/no) : ")).lower()
                    receiver_choose = Contact(accounts, account_found)
                    if receiver_choose:
                        if d1 == 'yes':
                            account_found.Transfer(d, receiver_choose)
                            Save_Accounts(accounts)
                            account_found.Back()
                        elif d1 == 'no':
                            account_found.Back()
                elif Choice == 7:
                    receiver_choose = Contact(accounts, account_found)
                    if receiver_choose:
                        receiver_choose.display_Historic_Receiver()
                        account_found.Back()
                elif Choice == 8:
                    print("Bye ! See u Later.")
                    print("=== Close To AppBank ===")
                    break