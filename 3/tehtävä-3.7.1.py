class Room:
    def __init__(self):
        self.room = []

    def add(self, person):
        self.room.append(person)

    def is_empty(self):
        if self.room == []:
            return True
        else:
            return False

    def print_contents(self):
        print("Here's everybody who's in the room at the moment: ")
        for person in self.room:
            print(person)


class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


room = Room()
print("Is the room empty?", room.is_empty())
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 175))
print("Is the room empty?", room.is_empty())
room.print_contents()
