import time
import math
import random


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
        if int(amount) > self.balance:
            print("Insufficient balance. ")
        else:
            self.balance -= int(amount)
            print(f"Withdrawal successful: {math.floor(self.balance)}")

    def interest(self):
        end_time = time.time()
        interest_rate = 0.05
        compound = (end_time - self.start_time) / 10
        if compound >= 1:
            self.balance = round(self.balance * ((1 + interest_rate) ** compound), 2)
            self.start_time = time.time()

    def bank_account(self):
        self.interest()
        print(math.floor(self.balance))


class StockMarket:

    def __init__(self):
        pass

    stocks = {
        "AAPL": 150.00,  # Apple
        "GOOGL": 2800.50,  # Alphabet (Google)
        "AMZN": 3400.25,  # Amazon
        "MSFT": 299.75,  # Microsoft
        "TSLA": 800.10,  # Teslaff
        "META": 315.30,  # Meta (Facebook)
        "NFLX": 410.45,  # Netflix
        "NVDA": 250.90,  # NVIDIA
        "ADBE": 650.60,  # Adobe
        "ORCL": 88.25,  # Oracle
    }

    # stock price cannot go to below than zero
    def simulate_market(self):
        for stock in self.stocks:
            # Random fluctuation between -10% and 10%
            fluctuation = random.uniform(-0.1, 0.1)
            self.stocks[stock] += self.stocks[stock] * fluctuation
            self.stocks[stock] = max(0, round(self.stocks[stock], 2))

    def __str__(self):
        self.simulate_market(self)
        stocks = ", ".join(
            [f"{stock}: ${price}" for stock, price in self.stocks.items()]
        )

        return f"Stock Prices: {stocks}"


class Portfolio:

    def __init__(self, account):
        self.account = account
        self.investments = {}

    def invest_stock(self):
        #  add stock to invested_stocks with the current price
        stock_name = input("Which stock do you want to invest? ")
        amount = input("How much do you want to invest? ")

        if stock_name not in StockMarket.stocks:
            print("Stock is not available. ")
        elif int(amount) <= 0:
            print("Investment amount must be greater than 0.")
        elif int(amount) <= self.account.balance:
            if stock_name in self.investments:
                StockMarket.simulate_market(self)

                # share quantity = amount / current price
                quantity = int(amount) / int(StockMarket.stocks[stock_name])
                self.investments[stock_name] += round(int(quantity), 4)
                self.account.balance -= int(amount)
            else:
                StockMarket.simulate_market(self)
                quantity = int(amount) / int(StockMarket.stocks[stock_name])
                self.investments[stock_name] = round(quantity, 4)
                self.account.balance -= int(amount)

            print(
                f"Bought {round(quantity, 4)} shares of {stock_name} with the price of {StockMarket.stocks[stock_name]}. New balance: ${self.account.balance}"
            )

    # Display portfolio
    def __str__(self):
        investments_str = ", ".join(
            [
                f"{stock}: {quantity} shares"
                for stock, quantity in self.investments.items()
            ]
        )
        return f"Portfolio of {self.account.owner}: {investments_str if investments_str else "No investments."}"

    # Display different Asset Class

    # Different investment vehicles, Stocks, Bonds, Real Estate


def main():
    customer_name = input("What is your name? ")
    deposit_amount = input("How much do you want to deposit? ")
    acc1 = Account(customer_name, deposit_amount)
    acc1_portfolio = Portfolio(acc1)
    stock_market = StockMarket()
    game_on = True

    actions = {
        "balance": acc1.bank_account,
        "deposit": lambda: acc1.deposit(int(input("Enter deposit amount: "))),
        "withdraw": lambda: acc1.withdraw(int(input("Enter withdraw amount: "))),
        "account": lambda: print(str(acc1)),
        "interest": acc1.interest,
        "invest": acc1_portfolio.invest_stock,
        "portfolio": lambda: print(str(acc1_portfolio)),
        "market": lambda: print(stock_market),
    }

    while game_on:
        user_input = input("What do you want to do? ")

        if user_input in actions:
            actions[user_input]()
        elif user_input == "stop":
            game_on = False
        else:
            print("Wrong input. Try again...")


if __name__ == "__main__":
    main()
