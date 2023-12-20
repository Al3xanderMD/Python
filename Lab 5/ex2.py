class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ${interest}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

savings_account = SavingsAccount("Petru", 1000, 0.02)
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.calculate_interest()
savings_account.display_balance()

checking_account = CheckingAccount("Bogdan", 500, 200)
checking_account.deposit(300)
checking_account.withdraw(700)
checking_account.display_balance()
