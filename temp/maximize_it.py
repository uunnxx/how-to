from functools import reduce

lst = [
    [7, 6429964, 4173738, 9941618, 2744666, 5392018, 5813128, 9452095],
    [7, 6517823, 4135421, 6418713, 9924958, 9370532, 7940650, 2027017],
    [7, 1506500, 3460933, 1550284, 3679489, 4538773, 5216621, 5645660],
    [7, 7443563, 5181142, 8804416, 8726696, 5358847, 7155276, 4433125],
    [7, 2230555, 3920370, 7851992, 1176871, 610460,  309961,  3921536],
    [7, 8518829, 8639441, 3373630, 5036651, 5291213, 2308694, 7477960],
    [7, 7178097, 249343,  9504976, 8684596, 6226627, 1055259, 4880436]
]


temp_list = list(map(sorted, lst))

print(temp_list)




# reduce(print, lst, 0)

#
# for i, e in enumerate(lst):
#     curr = e[i]
#
#     for j in lst[1:]:
#         for k in j:
#             print(k)




# def solver(lst):
#     list_of = []
#     max_result = 0
#
#     for i in lst:
#         for inner in i:
#             # list_of.append(reduce(max, i)**2)
#             inner
#
#
#
#     return sum(list_of) % 867
#
#
# print(solver(lst))
