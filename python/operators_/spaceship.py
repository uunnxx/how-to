# Ruby's spaceship operator <=>
# Where
#   if x > y then return 1
#   if x < y then return -1
#   if x = y then return 1
#   if a and b are not comparable then return nil


def spaceship(x: int, y: int) -> int:
    try:
        return (x > y) - (x < y)
    except TypeError:
        return None


print(spaceship(2, 1))
print(spaceship(1, 2))
print(spaceship(2, 2))
print(spaceship('a', 2))
