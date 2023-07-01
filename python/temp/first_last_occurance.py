# inputs = [int(x) for x in input("Enter multiple values: ").split()]
# find_out = int(input("What you want to find: "))


def first_last_occurance(lst, to_find):
    first = lst.index(to_find)
    # last = len(lst) - 1 - lst[::-1].index(to_find)
    last = lst.__len__() - lst[::-1].index(to_find) - 1
    return [first, last]


# print(first_last_occurance(inputs, find_out))


def dumd_version():
    first_occurance = None
    last_occurance = None
    find_out = 10
    index_counter = 0
    first_found = False

    while True:
        try:
            user_inp = int(input("Enter a value one by one: "))
            if user_inp == find_out:
                if first_found:
                    last_occurance = index_counter
                else:
                    first_occurance = index_counter
                    first_found = True

            index_counter += 1
        except ValueError:
            print([first_occurance, last_occurance])
            break

dumd_version()

