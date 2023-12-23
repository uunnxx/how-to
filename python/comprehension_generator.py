"""
Performance of str.join on a list comprehension vs generator expression

The string join is slightly faster on lists than on generators, though
likely not enough to matter most of the time.
"""
import timeit


def time(code, globals=globals()):
    return timeit.timeit(code, number=900, globals=globals)


numbers = range(1_000)
comprehension_join = time("""
joined = " ".join([str(n) for n in numbers])
""")
generator_expression_join = time("""
joined = " ".join(str(n) for n in numbers)
""")


print(f"{comprehension_join:.2f}s for list comprehension")
print(f"{generator_expression_join:.2f}s for generator expression")
