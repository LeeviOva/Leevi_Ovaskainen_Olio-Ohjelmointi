class LunchCard:

    def __init__(self, balance: float):
        self.balance = balance


    def __str__(self):
        return "The balance is {:.1f} euros".format(self.balance)

    def eat_ordinary(self):
        if self.balance < 2.95:
            print("You're lacking the credits buddy. No credits no food.")
        else:
            self.balance -= 2.95

    def eat_luxury(self):
        if self.balance < 5.90:
            print("You're lacking the credits buddy. No credits no food.")
        else:
            self.balance -= 5.90

    def deposit_money(self, amount:float):
        if amount < 0:
            raise ValueError("The deposit can't be negative im afraid :(")
        self.balance += amount


petercard = LunchCard(20)
gracecard = LunchCard(30)
petercard.eat_luxury()
gracecard.eat_ordinary()
print("Peter: ", petercard)
print("Grace: ", gracecard)
petercard.deposit_money(20)
gracecard.eat_luxury()
print("Peter: ", petercard)
print("Grace: ", gracecard)
petercard.eat_ordinary()
gracecard.deposit_money(50)
print("Peter: ", petercard)
print("Grace: ", gracecard)
