class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"Present: {self.name} ({self.weight}g)"





book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
print("The name of the present:", book.name)
print("The weight of the present:", book.weight)
print("Present:", book)