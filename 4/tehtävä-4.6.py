import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
        self.dice = Dice()

    def __str__(self):
        return f"Player {self.player_id}: {self.name}"

class Mammal:
    def __init__(self, species, name, size, weight):
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight


def play_game(num_players):
    players = [Player(f"Player {i}", i) for i in range(1, num_players + 1)]
    winning_sum = -1
    winning_player = None

    while winning_player is None:
        current_sum = 0
        for player in players:
            roll_sum = sum(player.dice.roll() for _ in range(3))
            print(f"{player.name} rolls: {roll_sum}")
            current_sum += roll_sum
            if roll_sum > winning_sum:
                winning_sum = roll_sum
                winning_player = player
            elif roll_sum == winning_sum:
                winning_player = None

    print(f"{winning_player.name} wins with a total of {winning_sum}!")


def select_pet_mammal(player):
    size = player.dice.roll() + player.dice.roll()  
    return Mammal("Dog", "Fido", size, size * 5)

def main():
    num_players = int(input("Enter the number of players: "))
    players = {i: Player(f"Player {i}", i) for i in range(1, num_players + 1)}

    for player_id, player in players.items():
        player.pet = select_pet_mammal(player)
        print(f"{player}\nPet Mammal: {player.pet.species} - {player.pet.name}")

 
    for player_id, player in players.items():
        print(f"{player.name}, it's your turn to select your pet mammal.")
        input("Press Enter to roll the dice...")
        selected_mammal = select_pet_mammal(player)
        player.pet = selected_mammal
        print(f"You got a {selected_mammal.species} named {selected_mammal.name}!")

if __name__ == "__main__":
    main()
