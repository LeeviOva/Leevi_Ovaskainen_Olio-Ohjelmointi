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




        
class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.suitcases = []

    def add_suitcase(self, suitcase):
        if self.total_weight() + suitcase.total_weight() <= self.max_weight:  # Corrected line
            self.suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.suitcases:
            print(f"Items in suitcase {suitcase}:")
            suitcase.print_items()


    def total_weight(self):
        return sum(suitcase.total_weight() for suitcase in self.suitcases)  # Corrected line

    def __str__(self):
        num_suitcases = len(self.suitcases)
        space_left = self.max_weight - self.total_weight()
        return f"{num_suitcases} suitcase{'s' if num_suitcases != 1 else ''}, space for {space_left} kg"




book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)

adas_suitcase = Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(1000)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(100)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()
