class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games

class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        return [game for game in super().list_games() if game.year < 1990]





museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("Age of war", "Louissi", 2007))
museum.add_game(ComputerGame("Minecraft", "Mojang", 2011))
for game in museum.list_games():
    print(game.name)
