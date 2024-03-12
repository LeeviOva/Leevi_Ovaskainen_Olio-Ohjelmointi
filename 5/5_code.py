class Mammal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self, food):
        print(f"{self.name} eats {food}, like a champ might I add")

    def sleep(self, hours):
        minutes = hours * 60
        print(f"{self.name} sleeps for {minutes} minutes")

    def move(self):
        print(f"{self.name} is moving")

class Cat(Mammal):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, age, gender)
        self.breed = breed

    def meow(self):
        print("Meow!")

class Dog(Mammal):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, age, gender)
        self.breed = breed

    def bark(self):
        print("Woof!")

class Dolphin(Mammal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def squeak(self):
        print("Eeeek! br. crazy tony")


cat = Cat("Megatron", 5, "male", "Persian")
dog = Dog("Bully", 3, "female", "Labrador")
dolphin = Dolphin("Crazy-Tony", 8, "male")

cat.eat("fish")
dog.sleep(8)
dolphin.move()
dolphin.squeak()
