
a = '8 11 -5 4 3 10'

def get_list(lst):
    lst = lst.split()

    def sort_list(lst):
        lst = map(int, lst)
        return sorted(lst)
    return sort_list


@get_list
