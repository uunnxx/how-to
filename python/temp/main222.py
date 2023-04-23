
def merge_arrays(arr1, arr2):
    '''
    распаковка *
    set {}
    sorted'll return list
    so no need to return explicitly list(sorted({*arr1, *arr2}))
    '''
    return sorted({*arr1, *arr2})

def merge_arrays2(arr1, arr2):
    return sorted(set(arr1 + arr2))


a, b = [0, 35, 36, 37, 6, 7, 8, 9, 10, 38], [-20, 39, 40, 50, -10, 25, -5, 62]


# print(merge_arrays(a, b))
# print(merge_arrays2(a, b))
#
# print({*a, *b})

def powers_of_two(num):
    return [2 ** i for i in range(num+1)]

def powers_of_two2(num):
    return [2**num for num in range(num+1)]

# print(powers_of_two2(4))



# print("string".capitalize())
# print("string".title())
#
#
# print(a)
# print(a[::-1])
# print(1 * 2 * 2)
# print(int(6.3 * 2 * 5))

print('-------------------------------------------------------------')

def set_alarm(emp, vac):
    return emp and (not vac)

# print(set_alarm(True, True))
# print(set_alarm(False, True))
# print(set_alarm(False, False))
# print(set_alarm(True, False))

print('-------------------------------------------------------------')



