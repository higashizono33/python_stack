class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print('User: {}, Balance: {}'.format(self.name, self.balance))
        return self
    def transfer_money(self, amount, toWhom):
        # self.toWhom = str(user)
        self.make_withdrawal(amount)
        toWhom.make_deposit(amount)
        self.display_user_balance()
        toWhom.display_user_balance()

#3 instances
user_1 = User("Mike", 100)
user_2 = User("Tom", 300)
user_3 = User("Jim", 200)

#user_1 transaction => using chaining methods
user_1.make_deposit(40).make_deposit(20).make_deposit(60).make_withdrawal(90).display_user_balance()

#user_2 transaction => using chaining methods
user_2.make_deposit(40).make_deposit(20).make_withdrawal(15).make_withdrawal(20).display_user_balance()

#user_3 transaction => using chaining methods
user_3.make_deposit(40).make_withdrawal(15).make_withdrawal(15).make_withdrawal(30).display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
# user_1.transfer_money(30, user_3)

