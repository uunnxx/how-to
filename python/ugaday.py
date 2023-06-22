import random


current = random.randint(1, 1000)

while True:

    user_choice = int(input('Type number from 1 to 1000: '))
    if user_choice == current:
        print(' ------------------ НАКОНЕЦ-ТО, СКА -------------------- ')
        break
    elif user_choice < current:
        print('Eshe bolshe')
    else:
        print('Menshe')
