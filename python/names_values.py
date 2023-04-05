
x += y
x = x + y          # conceptually
x = x.__iadd__(y)  # actually


# pseudo-code
class List:
    def __iadd__(self, other):
        self.extend(other)
        return self

# The same as:
num_list += [4, 5]
num_list.extend([4, 5]); num_list = num_list


board = [[0] * 8] * 8
board = [[0] * 8 for _ in range(8)]
