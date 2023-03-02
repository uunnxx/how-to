def recursion(count=10):
    print("Count:", count)
    if count == 0:
        return
    recursion(count-1)

recursion(count=15)
