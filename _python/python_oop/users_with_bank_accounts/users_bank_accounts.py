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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_1 = BankAccount(int_rate=0.01, balance=500)
        self.account_2 = BankAccount(int_rate=0.04, balance=1000)
    
    def make_deposit(self, amount, account):
        if account == 1:
            self.account_1.deposit(amount)
        if account == 2:
            self.account_2.deposit(amount)
        return self
    
    def make_withdrawal(self, amount, account):
        if account == 1:
            self.account_1.withdraw(amount)
        if account == 2:
            self.account_2.withdraw(amount)
        return self
    
    def display_user_balance(self, account):
        if account == 1:
            print('User: {}, account#1-Balance: {}'.format(self.name, self.account_1.balance))
        if account == 2:
            print('User: {}, account#2-Balance: {}'.format(self.name, self.account_2.balance))
        return self
    
    # def transfer_money(self, amount, toWhom):
    #     # self.toWhom = str(user)
    #     self.make_withdrawal(amount)
    #     toWhom.make_deposit(amount)
    #     self.display_user_balance()
    #     toWhom.display_user_balance()
    #     return self

user_1 = User("Tom", "tom@example.com")
user_1.make_deposit(500, 1).make_withdrawal(300, 2).display_user_balance(1).display_user_balance(2)