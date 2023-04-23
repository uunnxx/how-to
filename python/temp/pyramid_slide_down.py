#    /3/
#   \7\ 4
#  2 \4\ 6
# 8 5 \9\ 3

# 3 + 7 + 4 + 9 = 23

# input = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
# output = 23

# prev_index = 1

# first iteration [7, 4]
# compare(prev_index - 1, prev_index) return prev_index + 1 # 0 + 1

# second iteration [2, 4, 6]
# compare(prev_index - 1, prev_index) return prev_index + 1 # 1 + 1

# third iteration [8, 5, 9, 3]
# compare(prev_index - 1, prev_index) return prev_index + 1 # 2 + 1

def pyramid_slide_down2(lst):
    if len(lst) < 2:
        return 0

    prev_index = 1
    temp_list = [*lst[0]]


    for layer in lst[1:]:
        left_hand = layer[prev_index - 1]
        right_hand = layer[prev_index]

        if left_hand >= right_hand:
            temp_list.append(left_hand)
            prev_index -= 1
        else:
            temp_list.append(right_hand)
        prev_index += 1

    print(temp_list)
    print(sum(temp_list))

# test_case1 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
# test_case2 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3], [7, 6, 9, 1, 7]]
# test_case3 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3], [7, 6, 9, 1, 7], [9, 8, 1, 2, 4, 5]]

print()

def pyramid_slide_down(lst):
    if len(lst) < 2:
        return 0

    prev_index = 1
    temp_list = [*lst[0]]
    temp = 0
    prev_sum = lst[0][0]

    for index, layer in enumerate(lst[1:-1]):  # 1 to -1
        next_layer = lst[index+2]

        left_hand = layer[prev_index - 1]
        right_hand = layer[prev_index]

        child_left = next_layer[prev_index - 1]
        child_center = next_layer[prev_index]
        child_right = next_layer[prev_index + 1]

        first = prev_sum + left_hand + child_left
        second = prev_sum + left_hand + child_center
        third = prev_sum + right_hand + child_center
        fourth = prev_sum + right_hand + child_right

        dictionary = {'left_child_left': first, 'left_child_center': second, 'right_child_center': third, 'right_child_right': fourth}
        print(dictionary)
        print(max(dictionary, key=dictionary.get))
        max_value = max(dictionary, key=dictionary.get)

        if max_value in ['left_child_left', 'left_child_center']:
            temp_list.append(left_hand)
        elif max_value in ['right_child_center', 'right_child_right']:
            temp_list.append(right_hand)
        #
        print(f"{prev_sum=}")
        print(f"{layer=}")
        print(f"{next_layer=}")
        print()
        print(f"{left_hand=}")
        print(f"{right_hand=}")
        print()
        print(f"{child_left=}")
        print(f"{child_center=}")
        print(f"{child_right=}")
            #






            # if temp + n_left >= temp + n_right:
            #     temp_list.append(left_hand)
            #     temp_list.append(n_layer[prev_index-1])
            #     prev_index -= 1
            # elif temp + nn_left >= temp + nn_right:
            #     temp_list.append(left_hand)
            #     temp_list.append(n_layer[prev_index-1])
            #     prev_index -= 1
            #
            # else:
            #     temp_list.append(right_hand)
            #     temp_list.append(n_layer[prev_index])
            #
            # prev_index += 1

    print()
    print(f"{temp_list = }")
    # print(f"{sum(temp_list) = }")
    # print(f"{temp = }")
    # print(f"{result = }")
    print()

test_case4 = [
                                        [75],
                                      [95, 64],
                                    [17, 47, 82],
            #                       [18, 35, 87, 10],
            #                     [20,  4, 82, 47, 65],
            #                   [19,  1, 23, 75,  3, 34],
            #                 [88,  2, 77, 73,  7, 63, 67],
            #               [99, 65,  4, 28,  6, 16, 70, 92],
            #             [41, 41, 26, 56, 83, 40, 80, 70, 33],
            #           [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            #         [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            #       [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            #     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            #   [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            # [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            ]


# pyramid_slide_down(test_case1)
# pyramid_slide_down(test_case2)
# pyramid_slide_down(test_case3)
pyramid_slide_down(test_case4) # 1074

print()
print("should get 1074")

