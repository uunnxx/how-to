# from sample_package.sample_module import hello as h1
# from sample_package.sample_module2 import hello as h2
#
#
# h1()
# h2()


# people: list[str] = ['Mario', 'Luigi', 'Peach', 'Toad']
#
# for person in people:
#     if person == 'Luigi':
#         people.remove('Luigi')
        # people.append('TEST')
        # people.append('TEST2')
        # print(people)
        # print(person)

    # print('person: --> ', person)
    #
    # if person == 'Peach':
    #     print('Hi from Peach')
    #
    # print(f"{person} --> {people}")


# class Lamp:
#     def __init__(self, model: str, color: str):
#         self.model = model
#         self.color = color
#         self.state: bool = False
#
#     def turn_on(self):
#         print(f"{self.model} is turned on!")
#         self.state = True
#
#     def turn_off(self):
#         print(f"{self.model} is turned off!")
#         self.state = False
#
#     def __state(self):
#         return f"the lamp is {'on' if self.state else 'off'}"
#
#     def describe(self):
#         print(f"Lame: {self.model} ({self.color}) and {self.__state()}")
#
#
# red_lamp: Lamp = Lamp('br55', 'Red')
# blue_lamp: Lamp = Lamp('br55', 'Blue')
#
# lamps = [red_lamp, blue_lamp]
#
#
# for lamp in lamps:
#     lamp.turn_on()
#     lamp.describe()


class Fruit:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name
