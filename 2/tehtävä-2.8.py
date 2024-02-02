class Checklist:
    def __init__(self, header, entries):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, customer_id, balance, discount):
        self.id = customer_id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model, length, max_speed, bidirectional):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional
