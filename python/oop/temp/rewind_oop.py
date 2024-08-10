import itertools


class Car:
    def __init__(self, make: str, model: str, name: str):
        self.make = make
        self.model = model
        self.name = name

    def __str__(self) -> str:
        return f"{self.model}::{self.name} by {self.make} "


my_car = Car('Mazda', 'CVL', 'MX-5')


print(type(my_car))
print(my_car)


# -----------------------------------------------------------------------------

my_list_of_number = [i for i in range(1, 100) if i % 2 != 0]

divisible_by_3 = list(filter(lambda x: x % 3, my_list_of_number))

print(divisible_by_3)

print(len(my_list_of_number))


my_list_of_movies = ['Braveheart', 'Suprebad', 'PineappleExpress']
my_list_of_actors = ['Mel Gibson', 'Jonah Hill']

for (movie, actor) in zip(my_list_of_movies, my_list_of_actors):
    print(f"{movie} stars {actor}")


# for (movie, actor) in itertools.zip_longest(my_list_of_movies, my_list_of_actors):
#     print(f"{movie} stars {actor}")
