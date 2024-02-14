class LunchCard:

    def __init__(self, balance: float):
        self.balance = balance


    def __str__(self):
        return "The balance is {:.1f} euros".format(self.balance)


card = LunchCard(50)
print(card)