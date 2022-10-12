# Klassen und Objekte (Eigenes Beispiel)

# Klasse:

class Band:

    def __init__(self, genre: str, founding_year: int, singer: str, album1: str, favorite_album: str):
        self.genre = genre
        self.founding_year = founding_year
        self.singer = singer
        self.album1 = album1
        self.favorite_album = favorite_album

    @classmethod
    def definition(cls):
        print("Eine Band ist eine Gruppe von Musikern,"
              " die sich gemeinsam zusammenschließen und unter einem Namen Musik machen,"
              " normalerweise in Form von mehreren Songs in einem Album.")

# Klasse 2:


class Actor:

    def __init__(self, movies: str, favorite_movie: str):
        self.movies = movies
        self.favorite_movie = favorite_movie


# 1. Objekt (1. Band = Korn)

print("Korn:")

Korn = Band(genre="Metal",
            founding_year=1993,
            singer="Jonathan Davis",
            album1="Korn",
            favorite_album="The Serenity of Suffering")

print(Korn.genre)
print(Korn.founding_year)
print(Korn.singer)
print(Korn.album1)
print(Korn.favorite_album)


# 2. Objekt (2.Band = Three days grace)

print("Three Days grace:")

Three_Days_Grace = Band(genre="Alternative Metal",
                        founding_year=1992,
                        singer="Adam Gontier",
                        album1="Three Days Grace",
                        favorite_album="One-X")

print(Three_Days_Grace.genre)
print(Three_Days_Grace.founding_year)
print(Three_Days_Grace.singer)
print(Three_Days_Grace.album1)
print(Three_Days_Grace.favorite_album)


# 3. Objekt (3. Band = Motionless in White)

print("Motionless in White:")

Motionless_in_White = Band(genre="Metal",
                           founding_year=2005,
                           singer="Chris Motionless",
                           album1="Creatures",
                           favorite_album="Disguise")

print(Motionless_in_White.genre)
print(Motionless_in_White.founding_year)
print(Motionless_in_White.singer)
print(Motionless_in_White.album1)
print(Motionless_in_White.favorite_album)

