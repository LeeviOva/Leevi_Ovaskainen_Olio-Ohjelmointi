class NumberStats:
    def __init__(self):
        self.count = 0
        self.sum = 0

    def add_number(self, number: int):
        self.count += 1
        self.sum += number

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.sum

    def average(self):
        if self.count == 0:
            return 0
        return self.sum / self.count

if __name__ == "__main__":
    # Part 2 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
