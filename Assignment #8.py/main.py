from functions import BankAccount


def make_deposit(account):
    try:
        amount = float(input("How much would you like to deposit? $"))

        if account.deposit(amount):
            print(f"Deposit successful! New balance: ${account.balance:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    except ValueError:
        print("Invalid amount. Please enter a number.")


def make_withdrawal(account):
    try:
        amount = float(input("How much would you like to withdraw? $"))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif account.withdraw(amount):
            print(f"Withdrawal successful! New balance: ${account.balance:.2f}")
        else:
            print("Insufficient funds. You cannot withdraw more than your balance.")

    except ValueError:
        print("Invalid amount. Please enter a number.")


def view_account_information(account):
    account.display_account_info()



print("Welcome to the Bank!")

customer_name = input("Please enter your name: ")
account = BankAccount(customer_name)

while True:
    print("\nPlease choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        make_deposit(account)

    elif choice == "2":
        make_withdrawal(account)

    elif choice == "3":
        view_account_information(account)

    elif choice == "4":
        print("Thank you for your coming!")
        break

    else:
        print("Invalid choice. Please try again.")

