class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
        #alternatively
        #return super().withdraw(amount + self.withdraw_fee)

class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, account_type=Account):
        account = account_type(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for account in self.accounts:
            account.deposit(account.balance * account.interest)


#Multiple Inheritance
class SavingsAccount(Account):
    deposit_fee = 2
    
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1

supers = [c.__name__ for c in AsSeenOnTVAccount.mro()]
