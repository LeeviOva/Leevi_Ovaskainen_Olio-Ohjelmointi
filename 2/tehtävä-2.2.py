import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"

    def toss_the_coin(self):
        roll = random.randint(0,4)

        if roll == 0:
            self.sideup = "Heads"
        elif roll == 1:
            self.sideup = "Tails"
        elif roll == 2:
            self.sideup = "Sideways and upright :0"
        elif roll == 3:
            self.sideup = "The coin lands on the ground and is swallowed by a rabbithole, you're next."
        elif roll == 4:
            self.sideup = "The coin defies gravity and is sucked into a black whole in the process."


    def get_sideup(self):
        return self.sideup

def main():
    
    my_coin = Coin()

    print("This side is up: ", my_coin.get_sideup())

    print("Tossing the coin....")
    my_coin.toss_the_coin()

    print("Now this side is up: ",  my_coin.get_sideup())

main()