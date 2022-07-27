import random


class Account(object):
    def __init__(self, user_id, currency='USD'):
        self.user_id = user_id
        self.currency = currency
        self.currency_balance = self.__read_balance_from_database()
        print(f"Currency_balance is: {self.currency_balance}")

    def withdraw(self, amount):
        self.currency_balance = self.currency_balance - float(amount)
        print(f"New balance after withdraw: {self.currency_balance}")


    def deposit(self,amount):
        self.currency_balance = self.currency_balance + float(amount)
        print(f"New balance after deposit: {self.currency_balance}")

    def generate_statement(self, start_date, and_date):
        pass

    def __read_balance_from_database(self):
        print(f"Getting balance from db: {self.user_id}")
        return random.randint(100, 1000)


account1 = Account(9871)

import pdb; pdb.set_trace()



