class Item:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    def __str__(self):
        return f"{self._name} ({self._weight} g)"


class Suitcase:
    pass

class Cargohold:
    pass


book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
print("Name of the book:", book.name)
print("Weight of the book:", book.weight)
print("Book:", book)
print("Phone:", phone)
