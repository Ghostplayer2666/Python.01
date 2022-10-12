class A:
    def __init__(self):
        print("Konstruktor")

    def __str__(self):
        return "Klasse A"

    def __del__(self):
        print("Destruktur")


def myMain():
    print("Start")
    obj = A()
    print("Ende")
    print(obj)


if __name__ == "__main__":
    print("Start als Programm")
    # myMain()
