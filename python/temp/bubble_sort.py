def bubble_sort(array):
    for i in range(len(array)):

        # keep track of swapping
        swapped = False

        # loop to compare array elements
        for j in range(len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping occurs if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swapped = True
        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break


data = [-2, 45, 0, 11, -9]

bubble_sort(data)

print('Sorted Array in Ascending Order:')
print(data)
