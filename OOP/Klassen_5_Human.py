
class Human:

    n_humans = 0

    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.sex = sex

        Human.n_humans += 1

    def introduce(self):
        print("Hi! Mein Name ist " + self.name)

    @classmethod
    def counter(cls):
        return cls.n_humans

    @classmethod
    def definition(cls):
        print("Der Mensch, auch Homo Sapiens, ist ein intelligenteres Säugetier.")

    @staticmethod
    def add(number1: int, number2: int):
        return number1 + number2


Lisa = Human(name="Lisa",
             age=28,
             sex="W")

peter = Human(name="Peter",
              age=30,
              sex="M")

peter.introduce()
peter.definition()

peter.add(1, 2)


class Example:
    """Just a little example"""

    @staticmethod
    def static_method(*args):
        return args

    @classmethod
    def class_method(cls):
        return cls
