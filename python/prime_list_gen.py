import math
# def get_prime_numbers(lower, higher):
#     primes = []
#
#     for num in range(lower, higher + 1):
#         for prime in range(2, num + 1):
#             is_prime = True
#             for item in range(2, int(num ** .5) + 1):
#                 if num % item == 0:
#                     is_prime = False
#                     break
#
#     if is_prime:
#         primes.append(num)
#
# print(get_prime_numbers(30, 30_000))


def is_prime(num):
    for item in range(2, int(math.sqrt(num)) + 1):
        if num % item == 0:
            prime = False
    return prime


def get_prime_numbers(lower, higher):
    for possible_prime in range(lower, higher):
        if is_prime(possible_prime):
            yield possible_prime
        yield False


for prime in get_prime_numbers(30, 30_000):
    if prime:
        print(prime)



def get_all_users_age(total_users=1000):
    age = []
    for id in total_users:
        user_obj = access_db_to_get_user_by_id(id)
        age.append([user.name, user.age])
    return age


total_users = 1_000_000_000
for user_info in range(total_users):
    info = get_all_users_age()
    for user in info:
        print(user)
