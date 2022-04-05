# wite  a python program on bank account that has a balance and a list of transactions.

class bank_account:
    def __init__(self, balance):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(amount)

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(-amount)

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

a=bank_account(100)
a.deposit(50)
a.withdraw(20)
print(a.get_balance())
print(a.get_transactions())

