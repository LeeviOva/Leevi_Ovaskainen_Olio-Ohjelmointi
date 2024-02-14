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




stats = NumberStats()
while True:
    number = input("Please insert an integer: ")
    number = int(number)
    if number == -1:
        break
    stats.add_number(number)

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
