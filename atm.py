import pandas as pd
from account import Account
from utils.data_loader import load_user_data

class ATM:
    def __init__(self):
        self.user_data = load_user_data()
        self.current_account = None

    def start(self):
        print("Welcome to the ATM")
        self.authenticate_user()

    def authenticate_user(self):
        account_number = input("Please enter your account number: ")
        pin = input("Please enter your PIN: ")
        if self.validate_user(account_number, pin):
            self.account_menu()
        else:
            print("Invalid account number or PIN. Please try again.")
            self.authenticate_user()

    def validate_user(self, account_number, pin):
        user = self.user_data[(self.user_data['account_number'] == account_number) & (self.user_data['pin'] == pin)]
        if not user.empty:
            self.current_account = Account(user.iloc[0]['account_number'], user.iloc[0]['pin'], user.iloc[0]['balance'])
            return True
        return False

    def account_menu(self):
        while True:
            print("\n1. Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Select an option: ")
            if choice == '1':
                self.balance_inquiry()
            elif choice == '2':
                self.cash_withdrawal()
            elif choice == '3':
                self.cash_deposit()
            elif choice == '4':
                self.change_pin()
            elif choice == '5':
                self.transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def balance_inquiry(self):
        print(f"Your current balance is ${self.current_account.get_balance()}.")

    def cash_withdrawal(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.current_account.withdraw(amount):
            print(f"Withdrew ${amount}. Your new balance is ${self.current_account.get_balance()}.")
        else:
            print("Insufficient funds or invalid amount.")

    def cash_deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if self.current_account.deposit(amount):
            print(f"Deposited ${amount}. Your new balance is ${self.current_account.get_balance()}.")
        else:
            print("Invalid deposit amount.")

    def change_pin(self):
        new_pin = input("Enter your new PIN: ")
        if self.current_account.change_pin(new_pin):
            print("Your PIN has been changed successfully.")
        else:
            print("Invalid PIN. Please enter a 4-digit number.")

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.current_account.get_transaction_history():
            print(transaction)

if __name__ == "__main__":
    atm = ATM()
    atm.start()