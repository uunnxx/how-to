# There is a special way of receiving parameters to a function as a tuple or
# a dictionary using the * or ** prefix respectively.
# This is useful when taking variable number of arguments in the function.

def powersum(power, *args):
    '''Return the sum of each argument raised to the specified power.'''
    return sum(pow(i, power) for i in args)

powersum(2, 3, 4)
powersum(2, 10)

# Because we have a * prefix on the args variable, all extra arguments passed to
# the function are stored in `args` as a tuple. If a ** prefix had been used
# instead, the extra parameters would be considered to be key/value
# pairs of a dictionary.
