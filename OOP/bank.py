# Create a BankAccount class with deposit, withdraw, and get_balance methods & Add exception handling for overdrafts.
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")

    def get_balance(self):
        return self.balance
    
# Example usage:
account = BankAccount(100)  # Initial balance of $100
account.deposit(50)          # Deposit $50
account.withdraw(30)         # Withdraw $30
account.withdraw(150)        # Attempt to withdraw $150 (should fail)
print(f"Current Balance: ${account.get_balance():.2f}")  # Print current balance

