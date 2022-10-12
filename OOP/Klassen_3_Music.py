
class Music:
    def __init__(self):
        self.bands = None
        self.songs = None

    @classmethod
    def definition(cls):
        print("Musik ist eine wunderbare Erfindung der Menschen,"
              " die sehr vielfältig ist und sehr viele Menschen begeistert."
              "Es gibt unterschiedliche Arten der Musik, auch Genres genannt."
              "Diese 'Liste' von Musikarten und Beispielen soll nur ein ungefähres Beispiel darstellen."
              "Der Umfang von Musikarten und deren Bands ist um einiges größer.")


print("Metal:")

Metal = Music
Metal.bands = "Korn, Slipknot, BFMV, Avenged Sevenfold, Motionless in White, Seether, etc."
Metal.songs = "Rotting in Vain, Duality, Gravity, Buried Alive, Headache, Remedy, etc."

print("Bands:")
print(Metal.bands)
print("Songs:")
print(Metal.songs)


print("HipHop:")

HipHop = Music
HipHop.bands = "K.I.Z, Trailerpark, Marteria, etc."
HipHop.songs = "Walpurgisnacht, Falsche Band, Verstrahlt, etc."

print("Bands:")
print(HipHop.bands)
print("Songs:")
print(HipHop.songs)


print("Techno:")

Techno = Music
Techno.bands = "Timmy Trumpet, Blackgummy, etc."
Techno.songs = "Oracle, Machine, etc."

print("Bands:")
print(Techno.bands)
print("Songs:")
print(Techno.songs)


print("Rock:")

Rock = Music
Rock.bands = "Three Days Grace, Skillet, Hollywood Undead, Ghost etc."
Rock.songs = "Anonymous, Monster, Riot, etc."

print("Bands:")
print(Rock.bands)
print("Songs:")
print(Rock.songs)

print("Punk:")
Punk = Music
Punk.bands = "Shocky, Crystal F, Swiss"
Punk.songs = "Mein Licht, Deutschland, Wir Gegen Die"

