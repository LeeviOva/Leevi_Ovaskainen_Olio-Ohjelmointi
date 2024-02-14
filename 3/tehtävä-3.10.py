class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount:float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Your body is writing checks your bank account cannot cash")
        else:
            self.__balance -= amount
            self.__service_charge()

    def get_balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance -= self.__balance * 0.01


account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.get_balance())
account.deposit(100)
print(account.get_balance())