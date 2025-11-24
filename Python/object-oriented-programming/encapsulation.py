class BankAccount:
    def __init__(self, initial_balance):
        # Protected attribute (Convention: single leading underscore)
        # Suggests it should only be accessed or modified by class methods
        self._balance = initial_balance

    # Public Method to deposit funds
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    # Public Method (Getter) to access the protected balance
    def get_balance(self):
        return self._balance

# Create an object
account = BankAccount(100)
account.deposit(50)  # Safe modification via a method

# Direct access (Discouraged, but possible in Python)
# The underscore serves as a warning, not a strict lock
account._balance = 10000 
print(f"Balance after direct modification: ${account.get_balance()}")