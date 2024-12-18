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


def main():
    customer_name = input("What is your name? ")
    deposit_amount = input("How much do you want to deposit? ")
    acc1 = Account(customer_name, deposit_amount)
    game_on = True

    actions = {
        "balance": acc1.bank_account,
        "deposit": lambda: acc1.deposit(int(input("Enter deposit amount: "))),
        "withdraw": lambda: acc1.withdraw(int(input("Enter withdraw amount: "))),
        "account": lambda: print(str(acc1)),
        "interest": acc1.interest,
    }

    while game_on:
        user_input = input("What do you want to do? ")

        if user_input in actions:
            actions[user_input]()
        elif user_input == "stop":
            game_on = False
        else:
            print("Wrong input. Try again...")


main()
