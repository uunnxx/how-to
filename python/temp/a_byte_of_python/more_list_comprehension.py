listone = [2, 3, 4]
listtwo = [2 * i for i in listone if i > 2]
print(listtwo)


# How it works:
# Here, we derive a new list by specifying the manipulation to be done ( 2 * i )
# when some condition is satisfied ( if i > 2 ). Note that the original list
# remains unmodified.

# The advantage of using list comprehensions is that it reduces the amount of
# boilerplate code required when we use loops to process each element of a list
# and store it in a new list.
