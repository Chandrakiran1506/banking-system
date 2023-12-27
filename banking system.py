class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created successfully with an initial balance of {initial_balance}")
        else:
            print(f"Account {account_number} already exists. Please choose a different account number.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited {amount} into account {account_number}. New balance: {self.accounts[account_number]}")
        else:
            print(f"Account {account_number} not found. Please check the account number.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"Withdrew {amount} from account {account_number}. New balance: {self.accounts[account_number]}")
            else:
                print(f"Insufficient funds in account {account_number}.")
        else:
            print(f"Account {account_number} not found. Please check the account number.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account {account_number} balance: {self.accounts[account_number]}")
        else:
            print(f"Account {account_number} not found. Please check the account number.")


bank = Bank()

while True:
    print("\n==== Banking System ====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance (default is 0): "))
        bank.create_account(account_number, initial_balance)

    elif choice == "2":
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(account_number, amount)

    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(account_number, amount)

    elif choice == "4":
        account_number = input("Enter account number: ")
        bank.check_balance(account_number)

    elif choice == "5":
        print("Exiting the Banking System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
