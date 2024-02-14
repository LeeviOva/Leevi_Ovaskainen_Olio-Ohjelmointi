class NumberStats:
    def __init__(self):
        self.count = 0

    def add_number(self, number: int):
        self.count += 1

    def count_numbers(self):
        return self.count

if __name__ == "__main__":
    # Part 1 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())