import time
import math

from openpyxl.pivot.fields import Number


class Account:
    start_time = time.time()

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = int(balance)

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += int(amount)
        print(f"Deposit accepted {math.floor(self.balance)}")

    def withdraw(self, amount):
        if self.balance >= int(amount):
            self.balance -= int(amount)
            print(f"Withdrawal successful: {math.floor(self.balance)}")
        else:
            print("Funds Unavailable")

    def interest(self):
        end_time = time.time()
        interest_rate = 0.05
        compound = (end_time - self.start_time) / 10
        if compound >= 1:
            self.balance = self.balance * ((1 + interest_rate) ** compound)
            self.start_time = time.time()

    def bank_account(self):
        self.interest()
        print(math.floor(self.balance))


acc1 = Account("Jack", 5000)
game_on = True


while game_on:
    user_input = input("What do you want to do? ")
    if user_input == "balance":
        acc1.bank_account()
    elif user_input == "deposit":
        quantity = input()
        acc1.deposit(int(quantity))
    elif user_input == "withdraw":
        quantity = input()
        acc1.withdraw(quantity)
    elif user_input == "account":
        print(str(acc1))
    elif user_input == "interest":
        acc1.interest()
    elif user_input == "stop":
        game_on = False
    else:
        print("Wrong input. Try again...")
