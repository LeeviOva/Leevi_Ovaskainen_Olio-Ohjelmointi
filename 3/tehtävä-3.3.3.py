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


card = LunchCard(50)
print(card)

card.deposit_money(15)
print(card)
card.deposit_money(-1)
print(card)
