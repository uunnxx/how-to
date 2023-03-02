# s = 1
#
# while a := input():
#     try:
#         s *= int(a)
#     except ValueError:
#         print('Numbers only!')
#
# print(s)


city_list = input().split()

# for _, element in enumerate(city_list):
#     if len(element) < 5:
#         print('NO')
#         break
#     else:
#         print("YES")



def check(city):
    if len(city) < 5:
        print('NO')
        return
    else:
        print("YES")


a = list(map(check, city_list))
print(a)
