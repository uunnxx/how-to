nested = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

# здесь продолжайте программу

def get_line_list(nested_list ,flatten_list=[]):

    if len(nested_list) >= 2:
        head, tail = nested_list[0], nested_list[1:]
        get_line_list(tail)
    else:
        flatten_list.append(head)


    flatten_list.append(head)


    return flatten_list


print(get_line_list(nested))
