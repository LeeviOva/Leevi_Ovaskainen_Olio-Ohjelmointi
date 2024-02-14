class Recording:
    def __init__(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_length(self, value):
        self.__length = value


the_wall = Recording(43)
print(the_wall.get_length())
the_wall.set_length(44)
print(the_wall.get_length())
