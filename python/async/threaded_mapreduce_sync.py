from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor as Executor


def map_reduce_still_naive(my_input, mapper, reducer):
    with Executor() as executor:
        map_results = executor.map(mapper, my_input)

        distributor = defaultdict(list)
        for key, value in map_results:
            distributor[key].append(value)

        results = executor.map(reducer, distributor.items())
    return results


# Data          Map               Shuffle                Reduce     Result
#   ^            ^                   ^                     ^
# I fool at I    | (I, 1), (fool, 1) |                     |        (am, 2)
#                | (at, 1) (I, 1)    | (glad, 1) (of, 1)   |        (am, 2)
#                |                   | (fool, 1) (at, 1)   |        (glad, 1)
#                -                   | (weep, 1) (what, 1) |        (I, 2)
# am To what of  | (am, 1) (To, 1)   |                     |        (of, 1)
#                | (what, 1) (of, 1) |                     |        (a, 1)
#                |                   |                     |        (fool, 1)
#                -                   | (I, 1) (am, 1)      |        (at, 1)
# a weep glad am | (a, 1) (weep, 1)  | (am, 1) (a, 1)      |        (weep, 1)
#                | (glad, 1) (am, 1) | (I, 1) (to, 1)      |        (to, 1)
#                |                   |                     |        (what, 1)
