import tkinter as tk

class BankAccount():
    def __init__(self, name, balance, login, password):
        self.name = name
        self.balance = balance
        self.login = login
        self.password = password
        self.history = []
        self.history_Rec = []
        self.error = 3
        self.locked = False

    def Deposit(self, amount):
        if amount > 3500:
            return "Not Transaction"
        elif amount <= 0:
            return "Error Negative"
        self.balance += amount
        self.history.append(f"Deposit +{amount}€ | Balance : {self.balance:.2f}€")

    def Withdraw(self, amount):
        if amount > 600:
            return "Not Transact"
        elif amount <= 0:
            return "Error None"
        if amount > self.balance:
            return "Error Inssufisant"
        self.balance -= amount
        self.history.append(f"Withdraw -{amount}€ | Balance : {self.balance:.2f}€")

    def Transfer(self, amount, receiver_choose):
        if amount > 3500:
            return "Any Transfer"
        elif amount <= 0:
            return "Error False"
        if amount > self.balance:
            return "Money Ins"
        self.balance -= amount
        receiver_choose.balance += amount
        self.history.append(f"Transfer to {receiver_choose.name} -{amount}€ | Balance : {self.balance:.2f}€")
        receiver_choose.history_Rec.append(f"Transfer from {self.name} +{amount}€ | Balance : {receiver_choose.balance:.2f}€")

    def Display_History(self):
        return self.history

    def Display_History_Rec(self):
        return self.history_Rec

    def User_Log(self, Login):
        return Login == self.login
    
    def User_Password(self, Password):
        if self.error <= 0:
            self.locked = True

        if self.locked:
            print("Account Blocked !")
            return "Blocked"
        elif Password == self.password:
            print("Well Done")
            return "Well"
        
        if Password != self.password:
            self.error -= 1
            return "error"
        
def Loging(accounts, accnt):
    for account in accounts:
        if account.User_Log(accnt):
            return account
    return False

def Contact(accounts, account_found):
    receiver_possible = []
    for account in accounts:
        if account != account_found:
            receiver_possible.append(account)
    return receiver_possible

def Save_account(accounts):
    with open("accounts.txt", "w", encoding='utf-8') as file:
        for account in accounts:
            history_text = (";;").join(account.history)
            history_Rec_text = (";;").join(account.history_Rec)
            line = (account.name + "//"
                    + str(account.balance) + "//"
                    + account.login + "//"
                    + account.password + "//"
                    + str(account.error) + "//"
                    + str(account.locked) + "//"
                    + history_text + "//"
                    + history_Rec_text + "\n"
                    )
            file.write(line)

def Load_account():
    accounts = []

    try:
        with open("accounts.txt", "r", encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split("//")

                name = parts[0]
                balance = float(parts[1])
                login = parts[2]
                password = parts[3]
                error = int(parts[4])
                locked = parts[5] == 'True'

                history = parts[6].split(";;")
                history_Rec = parts[7].split(";;")

                if history == ['']:
                    history = []
                if history_Rec == ['']:
                    history_Rec = []

                account = BankAccount(name, balance, login, password)

                account.error = error
                account.locked = locked
                account.history = history
                account.history_Rec = history_Rec

                accounts.append(account)
    except FileNotFoundError:
        accounts = [
            BankAccount("Ali", 3000, "Alih@gm.com", "Alih4"),
            BankAccount("Ely", 4500, "Elyh@hm.com", "Elyh14"),
            BankAccount("Kayli", 5600, "KayLih@gm.com", "Kaylih4"),
            BankAccount("Yasmi", 7000, "Yasminh@gm.com", "Yasminh4")
            ]
        Save_account(accounts)
    return accounts

def Reset_account():
    accounts = [
        BankAccount("Ali", 3000, "Alih@gm.com", "Alih4"),
        BankAccount("Ely", 4500, "Elyh@hm.com", "Elyh14"),
        BankAccount("Kayli", 5600, "KayLih@gm.com", "Kaylih4"),
        BankAccount("Yasmi", 7000, "Yasminh@gm.com", "Yasminh4")
        ]
    Save_account(accounts)
    return accounts

accounts = Load_account()

def Info_Log():
    Log = Entry.get()
    Passwrd = Entry1.get()

    return Log, Passwrd

def Display_Check():
    Login, Passw = Info_Log()

    account_found = Loging(accounts, Login)
    if account_found:
        access = account_found.User_Password(Passw)
        Save_account(accounts)
        if access == 'Blocked':
            label = tk.Label(root, text="Account Blocked !!")
            label.pack()
            return False
        if access == 'Well':
            label1 = tk.Label(root, text="Well Done")
            label1.pack()
            return Menu_Interface(account_found)
        if access == 'error':
            label2 = tk.Label(root, text=f"Wrong Password or Login | Error Number : {account_found.error}")
            label2.pack()
            return False

def Menu_Interface(account_found):
    screen = tk.Toplevel()
    screen.title("Personal - BankAccount")
    screen.geometry("600x400")

    LabelName = tk.Label(screen, text=f"=== Welcome {account_found.name} ===", bg="Black", fg="White")
    LabelName.pack(pady=15)

    LabelAmount = tk.Label(screen, text=f"Amount : {account_found.balance:.2f}€", bg="Black", fg="White")
    LabelAmount.pack(pady=5)

    Button2 = tk.Button(screen, text="Deposit", command=lambda : Int_Deposit(account_found, LabelAmount))
    Button2.pack()
    Button3 = tk.Button(screen, text="Withdraw", command=lambda : Int_Withdraw(account_found, LabelAmount))
    Button3.pack()
    Button4 = tk.Button(screen, text="Transfer", command=lambda : Int_Transfer(account_found, LabelAmount))
    Button4.pack()
    Button5 = tk.Button(screen, text="Transaction History", command=lambda : Show_History(account_found))
    Button5.pack()
    Button6 = tk.Button(screen, text="Transfer Received", command=lambda : Show_Transaction_History(account_found))
    Button6.pack()
    Button7 = tk.Button(screen, text="Quit", command=screen.destroy)
    Button7.pack()

def Int_Deposit(account_found, LabelAmount):
    screen1 = tk.Toplevel()
    screen1.title("Make A Deposit")
    screen1.geometry("400x200")

    LabelValue = tk.Label(screen1, text="Insert a Value : ", bg="Black", fg="White")
    LabelValue.pack(pady=5, side="top")

    frame = tk.Frame(screen1)
    frame.pack()
    Entry3 = tk.Entry(frame)
    Entry3.pack(side="left")
    tk.Label(frame, text="€").pack(side="left")

    Button4 = tk.Button(screen1, text="Confirm", command=lambda : Apply_Deposit(account_found, Entry3, LabelAmount))
    Button4.pack(pady=5)
    Button5 = tk.Button(screen1, text="Back", command=screen1.destroy)
    Button5.pack(pady=5)

def Int_Withdraw(account_found, LabelAmount):
    screen2 = tk.Toplevel()
    screen2.title("Make A Withdraw")
    screen2.geometry("400x200")

    LabelValue1 = tk.Label(screen2, text="Insert a Value : ", bg="Black", fg="White")
    LabelValue1.pack(pady=5)

    frame1 = tk.Frame(screen2)
    frame1.pack()
    Entry4 = tk.Entry(frame1)
    Entry4.pack(side="left")
    tk.Label(frame1, text="€").pack(side="left")

    Button6 = tk.Button(screen2, text="Confirm", command=lambda : Apply_Withdraw(account_found, Entry4, LabelAmount))
    Button6.pack(pady=5)
    Button7 = tk.Button(screen2, text="Back", command=screen2.destroy)
    Button7.pack(pady=5)

def Int_Transfer(account_found, LabelAmount):
    screen3 = tk.Toplevel()
    screen3.title("Make A Transfer")
    screen3.geometry("400x200")

    LabelValue2 = tk.Label(screen3, text="Insert a Value : ", bg="Black", fg="White")
    LabelValue2.pack(pady=5)
    frame2 = tk.Frame(screen3)
    frame2.pack()
    Entry5 = tk.Entry(frame2)
    Entry5.pack(side="left")
    tk.Label(frame2, text="€").pack(side="left")

    Button8 = tk.Button(screen3, text="Confirm/open", command=lambda : Apply_Transfer(account_found, Entry5, LabelAmount))
    Button8.pack(pady=10)
    Button9 = tk.Button(screen3, text="Back", command=screen3.destroy)
    Button9.pack(pady=5)

def Show_History(account_found):
    screen4 = tk.Toplevel()
    screen4.title("History")
    screen4.geometry("400x300")

    watch = account_found.Display_History()

    if not watch:
        tk.Label(screen4, text="Not History Yet", bg="Cyan", fg="Black").pack()
    else:
        for element in watch:
            tk.Label(screen4, text=element).pack(anchor="w", padx=15)

    Button10 = tk.Button(screen4, text="Back", command=screen4.destroy)
    Button10.pack(pady=5)

def Show_Transaction_History(account_found):
    screen5 = tk.Toplevel()
    screen5.title("Transaction History")
    screen5.geometry("400x300")

    Rec = account_found.Display_History_Rec()

    if not Rec:
        tk.Label(screen5, text="Not Transaction History Yet", bg="Cyan", fg="Black").pack()
    else:
        for element in Rec:
            tk.Label(screen5,
                text=element
            ).pack(anchor="w", padx=10)
    
    Button11 = tk.Button(screen5, text="Back", command=screen5.destroy)
    Button11.pack(pady=5)
    
def Apply_Deposit(account_found, Entry3, LabelAmount):
    try:
        Amount = float(Entry3.get())
    except ValueError:
        return

    result = account_found.Deposit(Amount)

    if result == "Not Transaction" or result == "Error Negative":
        return
    
    LabelAmount.config(text=f"Amount : {account_found.balance:.2f}")
    Save_account(accounts)

def Apply_Withdraw(account_found, Entry4, LabelAmount):
    try:
        Amount = float(Entry4.get())
    except ValueError:
        return
    
    result = account_found.Withdraw(Amount)
    
    if result == "Not Transact" or result == "Error None" or result == "Error Inssufisant":
        return

    LabelAmount.config(text=f"Amount : {account_found.balance:.2f}")
    Save_account(accounts)

def Apply_Transfer(account_found, Entry5, LabelAmount):
    try:
        Amount = float(Entry5.get())
    except ValueError:
        return
    
    screen6 = tk.Toplevel()
    screen6.title("List Transfer")
    screen6.geometry("200x300")

    receivers = Contact(accounts, account_found)
    for receiver in receivers:
        Button12 = tk.Button(screen6,
            text=receiver.name,
            command=lambda r=receiver: List_Contact(account_found, Amount, r, LabelAmount, screen6)
        )
        Button12.pack()

    Button13 = tk.Button(screen6, text="Back", command=screen6.destroy)
    Button13.pack(pady=5) 

def List_Contact(account_found, Amount, r, LabelAmount, screen4):
    account_found.Transfer(Amount, r)
    Save_account(accounts)
    LabelAmount.config(text=f"Amount : {account_found.balance:.2f}€")
    screen4.destroy()

root = tk.Tk()
root.title("Atm - BanKAccount")
root.geometry("720x560")

LabelTitle = tk.Label(root, text='=== Welcome To AppBank ===', bg="Black", fg="White")
LabelTitle.pack(pady=20)
LabelSub = tk.Label(root, text='Enter Login')
LabelSub.pack()
Entry = tk.Entry(root)
Entry.pack()

LabelSub1 = tk.Label(root, text='Enter Password')
LabelSub1.pack(pady=5)
Entry1 = tk.Entry(root, show="*")
Entry1.pack()

Button = tk.Button(root, text='Login', command=Display_Check)
Button.pack(pady=10)
Button1 = tk.Button(root, text='Leave', command=root.destroy)
Button1.pack()

root.mainloop()