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

card = LunchCard(50)
print(card)

card.eat_ordinary()
print(card)

card.eat_luxury()

print(card)