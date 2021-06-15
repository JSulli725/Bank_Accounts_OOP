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

checking_account = BankAccount(0 , 0.005)
savings_account = BankAccount(0 , 0.03)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0 , .002)

    # def make_deposit(self, amount):
    #     self.account.deposit += amount
    #     return self

    # def make_withdrawal(self, amount):
    #     self.account.withdraw -= amount
    #     return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account}")

    def transfer_money(self, other_user , amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        self.amount_transferred = amount

user1 = User("Bill" , "billybob@google.com")
user2 = User("George" , "georgepwney@att.net")
user3 = User("Sue" , "sue.heckleschmidt@abcfarms.com")

print(f"User: {user1.name}")
user1.account.deposit(20).deposit(100).deposit(50).withdraw(75)
print(f"Balance: {user1.account.balance}")
print()
print(f"User: {user2.name}")
user2.account.deposit(60).deposit(110).withdraw(12).withdraw(75)
print(f"Balance: {user2.account.balance}")
print()
print(f"User: {user3.name}")
user3.account.deposit(45).withdraw(12).withdraw(3).withdraw(9)
print(f"Balance: {user3.account.balance}")
print()
user1.transfer_money(user3, 10)
print(f"{user1.name} transferred ${user1.amount_transferred} to {user3.name}.\n{user1.name} now has ${user1.account.balance} \n{user3.name} now has ${user3.account.balance}")