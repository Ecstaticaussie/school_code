class Account:
    def __init__(self, number, holder_name, balance):
        self.number = number
        self.holder_name = holder_name
        self.balance = balance

    def withdraw(self, amount):
        self.balance += amount

    def deposit(self, amount):
        self.balance -= amount

    def __str__(self):
        print(f"\nName: {self.holder_name}\nNumber: {self.number}\nBalance: £{self.balance}")

class SavingsAccount(Account):
    def __init__(self, interest_rate, number, holder_name, balance):
        super().__init__(number, holder_name, balance)
        self.interest_rate = interest_rate

class CheckingAccount:
    def __init__(self, transaction_fee, number, holder_name, balance):
        super().__init__(number, holder_name, balance)
        self.transaction_fee = transaction_fee

class Bank:
    def __init__(self):
        self.all_accounts = []

    def setup(self, accounts):
        for account in accounts: self.all_accounts.append(account)

    def show_all_accounts(self):
        for account in self.all_accounts: print(account)

    def calc_total_bal(self):
        self.total_bal = sum([account.balance for account in self.all_accounts])

    def calc_avg_bal(self):
        self.avg_bal = round(self.total_bal / len(self.all_accounts) , 2)


accounts = []

bank_of_murica = Bank()
lloyd = Bank()
monzo = Bank()
