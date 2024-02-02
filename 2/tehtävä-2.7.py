class Movie:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year


once_upon_a_time_in_hollywood = Movie(name="Once upon a time in Hollywood", director="Quentin Tarantino", genre ="Comedy(?)", year = "2019")
godfather = Movie(name="The Godfather", director="Francis Ford Coppola", genre ="mafia/action", year = "1972")


print(f"{once_upon_a_time_in_hollywood.director} {once_upon_a_time_in_hollywood.genre} {once_upon_a_time_in_hollywood.year}  ")
print(f"{godfather.name}: {godfather.director} {godfather.genre} {godfather.year} ")