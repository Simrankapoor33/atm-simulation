class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def change_pin(self, new_pin):
        if new_pin.isdigit() and len(new_pin) == 4:
            self.pin = new_pin
            return True
        return False

    def get_transaction_history(self):
        return self.transaction_history