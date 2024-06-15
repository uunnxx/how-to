def countways_(bills, amount, index):
    if amount == 0:  # base case 1
        return 1
    if amount < 0 or index >= len(bills):  # base case 2
        return 0
    # count the number of ways to make amount by including bills[index] and excluding bills[index]
    return (
        countways_(bills, amount - bills[index], index) +
        countways_(bills, amount, index+1)
    )


def countways(bills, amount):
    return countways_(bills, amount, 0)


print(countways([1, 2, 5], 5))
