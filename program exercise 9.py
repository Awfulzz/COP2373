# BankAcct Class Assignment
# This program creates a BankAcct class and tests its methods.


class BankAcct:
    """A simple bank account class."""

    def __init__(self, name, account_number, amount, interest_rate):
        """Initialize the bank account with owner info and starting values."""
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        """Adjust the interest rate for the account."""
        self.interest_rate = new_rate

    def deposit(self, deposit_amount):
        """Deposit money into the account."""
        if deposit_amount > 0:
            self.amount += deposit_amount
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, withdraw_amount):
        """Withdraw money from the account."""
        if withdraw_amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif withdraw_amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= withdraw_amount

    def give_balance(self):
        """Return the current balance."""
        return self.amount

    def calculate_interest(self, days):
        """Calculate interest based on the number of days."""
        interest = self.amount * (self.interest_rate / 100) * (days / 365)
        return interest

    def __str__(self):
        """Return a string showing the account balance and interest rate."""
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2f}%")


def test_bank_account():
    """Test function for the BankAcct class."""

    # Create a bank account object
    acct1 = BankAcct("Alex Bowles", "123456789", 1000.00, 2.5)

    # Display initial account information
    print("Initial Account Information:")
    print(acct1)
    print()

    # Test deposit
    print("Depositing $250.00...")
    acct1.deposit(250.00)
    print(f"New Balance: ${acct1.give_balance():.2f}")
    print()

    # Test withdrawal
    print("Withdrawing $100.00...")
    acct1.withdraw(100.00)
    print(f"New Balance: ${acct1.give_balance():.2f}")
    print()

    # Test insufficient funds
    print("Attempting to withdraw $2000.00...")
    acct1.withdraw(2000.00)
    print()

    # Test adjusting interest rate
    print("Adjusting interest rate to 3.0%...")
    acct1.adjust_interest_rate(3.0)
    print(acct1)
    print()

    # Test interest calculation
    days = 30
    interest = acct1.calculate_interest(days)
    print(f"Interest for {days} days: ${interest:.2f}")
    print()


def main():
    """Main function to run the test."""
    test_bank_account()


if __name__ == "__main__":
    main()
