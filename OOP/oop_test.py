# Klasse 1
class Human:
    def __init__(self, age: int, name: str, birth: int):
        self.age = age
        self.name = name
        self.birth = birth


# Objekt 1 Klasse Human
Ghost = Human(age=19,
              name="Annelie",
              birth=2003)

# Objekt 2 Klasse Human
Dennis = Human(age=21,
               name="Dennis",
               birth=2001)


# Klasse 2
class Food:
    def __init__(self):
        self.ingredient1 = None
        self.ingredient2 = None
        self.ingredient3 = None


# Objekt 1 Klasse Food
Pizza = Food
Pizza.ingredient1 = "Tomato"
Pizza.ingredient2 = "Cheese"
Pizza.ingredient3 = "Pineapple"
