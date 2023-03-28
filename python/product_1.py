from itertools import product


lst_1 = [1, 25, 67, 22]
lst_2 = [20, 50, 100]
lst_3 = [30, 10, 30, 11]

for a, b, c in product(lst_1, lst_2, lst_3):
    if a + b + c == 61:
        print('got it')


###############################################################################


for a in lst_1:
    for b in lst_2:
        for c in lst_3:
            if a + b + c == 61:
                print('got it')
