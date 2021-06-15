class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, other_user , amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.amount_transferred = amount

user1 = User("Bill" , "billybob@google.com")
user2 = User("George" , "georgepwney@att.net")
user3 = User("Sue" , "sue.heckleschmidt@abcfarms.com")

user1.make_deposit(20).make_deposit(100).make_deposit(50).make_withdrawal(75)
print(f"User: {user1.name} \n Balance: {user1.account_balance}")

user2.make_deposit(60).make_deposit(110).make_withdrawal(12).make_withdrawal(75)
print(f"User: {user2.name} \n Balance: {user2.account_balance}")

user3.make_deposit(45).make_withdrawal(12).make_withdrawal(3).make_withdrawal(9)
print(f"User: {user3.name} \n Balance: {user3.account_balance}")

user1.transfer_money(user3, 10)
print(f"{user1.name} now has ${user1.account_balance} \n{user3.name} now has ${user3.account_balance}")

