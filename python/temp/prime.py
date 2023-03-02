def is_prime(num):
    if num == 2 or num == 3: return True
    if num < 2 or num % 2 == 0: return False
    if num < 9: return True
    if num % 3 == 0: return False

    k = 3
    while k*k <= num:
        if num % k == 0:
            return False
        k +=2
    return True


print(is_prime(87))
print(is_prime(20))
print(is_prime(19))
