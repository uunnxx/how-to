# import os
#
#
# if not os.path.exists('cities.txt'):
#     os.mknod('cities.txt')
#

# cities = ['Adelaide', 'Alice Springs', 'Darwin', 'Melbourne', 'Sydney']
#
# with open('city_files.txt', 'w') as city_files:
#     for city in cities:
#         print(city, file=city_files)

cities = []

with open('city_files.txt', 'r') as city_files:
    for city in city_files:
        cities.append(city.rstrip())


for i in cities:
    print(i)
