
# Klassen und Objekte:    (Beispiel)


# Klasse:

class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None


# Erstes objekt:

car1 = Car()
print(car1.car_brand)
car1.car_brand = "Audi"
car1.horse_power = 250
car1.color = "black"

print(car1.car_brand)
print(car1.horse_power)
print(car1.color)


# Zweites Objekt:

car2 = Car()
print(car2.car_brand)
car2.car_brand = "Porsche"
car2.horse_power = 300
car2.color = "red"

print(car2.car_brand)
print(car2.horse_power)
print(car2.color)


# Referenz = Objekt-Adressen:

print(car1)
print(car2)
