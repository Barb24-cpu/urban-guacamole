"""
Abstractions.
Bank Class->
deposits, withdral,
show account.
getter and setter. ->
-> easy to scale function <understing>

-> Login account
-> Create account
-> Deposit
-> Withdrawal
-> account balance
"""

class BankAccount:

    def __init__(self, name, balance, account_no):
        self.name = name
        self._balance = balance
        self.account_no = account_no

    # data i read
    @property
    def balance(self):
        print("somebody tried to read johns balance")
        return self._balance

    # to control updated
    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            print("Ensure you pass a number for new balance")
            return
        if value < 0:
            print("Ensure new balance must not be less than 0")
            return
        self._balance = value

    # setter
    def deposit(self):
        pass

    def withdrawal(self):
        pass

    def show_account_details(self):
        print(f"Owner {self.name}")
        print(f"Balance {self.balance}")
        print(f"Account No {self.account_no}")


john = BankAccount(name="John Mwangi", balance=0, account_no="223344223")

print("John blance ", john.balance)
# john.show_account_details()
# it is easily accessable ->
# john.balance=-5000 #setting - undating the property