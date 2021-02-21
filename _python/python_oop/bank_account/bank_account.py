class BankAccount:
    def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
        # your code here! (remember, this is where we specify the attributes for our class)
        if not balance:
            self.balance = 0
        else:
            self.balance = balance
        self.int_rate = int_rate
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self
    def display_account_info(self):
        # your code here
        print('Balance: {}'.format(self.balance))
        return self
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

# Create 2 accounts
user_1 = BankAccount(0.04, 500)
user_2 = BankAccount(0.01, 1000)

# To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
user_1.deposit(300).deposit(200).deposit(100).withdraw(300).yield_interest().display_account_info()
# To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
user_2.deposit(300).deposit(200).withdraw(100).withdraw(300).withdraw(100).withdraw(300).yield_interest().display_account_info()
