from collections import defaultdict


def map_reduce_ultra_naive(my_input, mapper, reducer):
    map_results = map(mapper, my_input)

    shuffler = defaultdict(list)
    for key, value in map_results:
        shuffler[key].append(value)

    return map(reducer, shuffler.items())


# emitter = lambda word: (word, 1)
def emitter(word):
    return (word, 1)


# counter = lambda (word, emissions): (word, sum(emissions))
def counter(item):
    # map |word, emissions| do
    #     (word, sum(emissions))
    # end
    word, emissions = item
    return (word, sum(emissions))


words = 'Python is great Python rocks'.split()
print(list(map_reduce_ultra_naive(words, emitter, counter)))
