class BankAccount:
    def __init__(self, owner, balance=0) -> None:
        self.owner = owner
        self.balance = balance
        print(f"Account Created! Below are details,\nAccount Holder Name: {self.owner}\nInital Balance:{self.balance}")

    def __str__(self) -> str:
        return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance}"
    def deposit(self,amt):
        self.balance += amt
        print(f"SUCCESS! Current Balance is {self.balance}")

    def withdraw(self,amt):
        if amt <= self.balance:
            self.balance -= amt
            print(f"SUCCESS! Current Balance is {self.balance}")
        else:
            print("Balance Low! Amount cannot be deducted")

acct1 = BankAccount("Jose", 100)
acct1.deposit(10)
acct1.withdraw(300)
acct1.deposit(30)
acct1.withdraw(50)
print(acct1)
# print(acct1.balance)
