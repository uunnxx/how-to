from math import factorial


def pascal_triangel(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=' ')
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=' ')
        print()



pascal_triangel(8)
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
