def br():
    print(f"\n{'-' * 80}\n")


class Car:
    def __init__(self, name, color=None, type_of_car=None, year=None):
        self.name = name
        self.color = color
        self.type_of_car = type_of_car
        self.year = year
        self.ENGINE = False

    def check_engine(self):
        if self.ENGINE:
            print("The engine of the car is running and the car is ready for the trip")
        else:
            print("To go, you need to turn on the engine")

    def turn_engine_on(self):
        self.ENGINE = True

    def turn_engine_off(self):
        self.ENGINE = False

    def __str__(self):
        return (
            "Information about the car:"
            f"\n\tName: {self.name}"
            f"\n\tColor: {self.color}"
            f"\n\tYear: {self.year}"
            f"\n\tType: {self.type_of_car}"
        )


porche = Car('Porche', "red", "sport", 2022)
ford = Car('Ford', 'blue', 'sport', 2020)

br()

porche.check_engine()
porche.turn_engine_on()
porche.check_engine()
print(porche)
print(porche.__dict__)

br()

ford.check_engine()
ford.turn_engine_on()
ford.check_engine()
print(ford)
print(ford.__dict__)

br()
