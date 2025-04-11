############################################################################
# You already know to use the list selection [x,y][b] with a Boolean b for
# the ternary expression y if b else x.
# The variables x, y, and b can also be expressions,
# though note that both x and y are evaluated even when not selected.

# Here's some potential optimizations when x and y are numbers.

# [0,y][b]   -> y*b
# [1,y][b]   -> y**b
# [x,1][b]   -> b or x
# [x,x+1][b] -> x+b
# [x,x-1][b] -> x-b
# [1,-1][b]  -> 1|-b
# [x,~x][b]  -> x^-b
# [x,y][b]   -> x+z*b (or y-z*b), where z=y-x.
# [-x,~x][b] -> -x-b

# You can also switch x and y if you can rewrite b to be its negation instead.


############################################################################


# PEP448 – Additional Unpacking Generalizations
# With the release of Python 3.5, manipulation of lists,
# tuples, sets and dicts just got golfier.
#
# Turning an iterable into a set/list
# Compare the pairs:
#
# set(T)
# {*T}
#
# list(T)
# [*T]
#
# tuple(T)
# (*T,)
# Much shorter! Note, however, that if you just want to convert
# something to a list and assign it to a variable,
# normal extended iterable unpacking is shorter:
#
# L=[*T]
# *L,=T
# A similar syntax works for tuples:
#
# T=*L,
# which is like extended iterable unpacking,
# but with the asterisk and comma on the other side.
#
# Joining lists/tuples
# Unpacking is slightly shorter than concatenation if you need
# to append a list/tuple to both sides:
#
# [1]+T+[2]
# [1,*T,2]
#
# (1,)+T+(2,)
# (1,*T,2)
# Printing the contents of multiple lists
# This isn't limited to print, but it's definitely
# where most of the mileage will come from.
# PEP448 now allows for multiple unpacking, like so:
#
# >>> T = (1, 2, 3)
# >>> L = [4, 5, 6]
# >>> print(*T,*L)
# 1 2 3 4 5 6
# Updating multiple dictionary items
# This probably won't happen very often, but the syntax can be used
# to save on updating dictionaries if you're updating at least three items:
#
# d[0]=1;d[1]=3;d[2]=5
# d={**d,0:1,1:3,2:5}
# This basically negates any need for dict.update.
