class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("You don't have enough funds")
            return False

    

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.ordinaries = 0
        self.luxuries = 0

    def eat_ordinary(self, payment: float):
        if payment >= 2.95:
            self.funds += 2.95
            self.ordinaries += 1
            change = payment - 2.95
        else:
            change = payment
        return change


    def eat_luxury(self, payment: float):
        if payment >= 5.90:
            self.funds += 5.90
            self.luxuries += 1
            change = payment - 5.90
        else:
            change = payment
        return change


    def eat_ordinary_lunchcard(self, card: LunchCard):
        if card.balance >= 2.95:
            self.funds += 2.95
            card.balance -= 2.95
            self.ordinaries += 1
            return True
        else:
            return False



    def eat_luxury_lunchcard(self, card: LunchCard):
        if card.balance >= 5.90:
            self.funds += 5.90
            card.balance -= 5.90
            self.luxuries += 1
            return True
        else:
            return False
    
    def deposit_money_on_card(self, card: LunchCard, amount: float):
        if amount > 0:
            self.funds += amount
            card.balance += amount
        else:
            print("it cant be zero silly")


#You may use the following code to test your function:

if __name__ == "__main__":

    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.ordinaries)
    print("Special lunches sold:", exactum.luxuries)