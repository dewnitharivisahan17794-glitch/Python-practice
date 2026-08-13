#Encapsulation
# Encapsulation is the concept of wrapping data and methods that operate on that data within a single unit,
#  such as a class. It helps to protect the internal state of an object from unintended interference and misuse.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute(dubble underscore before the attribute name indicates that it is private and should not be accessed directly from outside the class.)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

balance = BankAccount("123456789", 1000)
print(balance.get_balance())
print(balance.deposit(500))
print(balance.withdraw(200))
print(balance.get_balance())
print(balance.__balance)  # This will raise an AttributeError because __balance is private and cannot be accessed directly from outside the class.
