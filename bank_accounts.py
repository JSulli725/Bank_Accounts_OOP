class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.total_interest = 0

    def deposit(self, amount):
        self.balance += amount
        print("deposited", amount)
        return self

    def withdraw(self, amount):
        self.balance -= amount
        print("withdrew", amount)
        if(amount > self.balance):
            self.balance - 5
            print("Insufficient funds: charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if(self.balance > 0):
            self.total_interest += self.balance * self.interest_rate
            self.balance += self.balance * self.interest_rate
        else:
            print("No money in account or negative balance detected. No interest generated.")
        print(f"Total interest generated is: ${self.total_interest}")
        return self


account1 = BankAccount(0 , 0.029)
account2 = BankAccount(0 , 0.015)

print("\naccount1:")
account1.deposit(25).deposit(40).deposit(33).withdraw(13).yield_interest().display_account_info()


print("\naccount2:")
account2.deposit(50).deposit(27).withdraw(12).withdraw(13).withdraw(8).withdraw(6).yield_interest().display_account_info()