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
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []
    
    def add_item(self, item):
        if self.total_weight() + item.weight <= self.max_weight:
            self.items.append(item)

    def print_items(self):
        for item in self.items:
            print(item)

    def weight(self):
        return sum(item.weight for item in self.items)

    def total_weight(self):
        return sum(item.weight for item in self.items)

    def heaviest_item(self):
        if not self.items:
            return None
        return max(self.items, key=lambda x: x.weight)

    def __str__(self):
        num_items = len(self.items)
        if num_items == 1:
            item_text = "1 item"
        else:
            item_text = f"{num_items} items"
        return f"{item_text} ({self.total_weight()} g)"


        
class Cargohold:
    pass


book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)
suitcase = Suitcase(500)
print(suitcase)
suitcase.add_item(book)
print(suitcase)
suitcase.add_item(phone)
print(suitcase)
suitcase.add_item(brick)
print(suitcase)