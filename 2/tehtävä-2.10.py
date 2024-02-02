class Movie:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year
def movies_of_genre(movies, genre):
    return [movie for movie in movies if movie.genre == genre]




once_upon_a_time_in_hollywood = Movie(name="Once upon a time in Hollywood", director="Quentin Tarantino", genre ="Action", year = "2019")
godfather = Movie(name="The Godfather", director="Francis Ford Coppola", genre ="Action", year = "1972")
barbie = Movie(name="Barbie", director="Greta Gerwig", genre = "Comedy", year ="2023")

movies = [once_upon_a_time_in_hollywood, godfather]
print("Movies in action genre: ")

for movie in movies_of_genre(movies, "Action"):
    print(f"{movie.director}: {movie.name}")