import string
import timeit


class BadHash(str):
    def __hash__(self) -> int:
        return 42


class GoodHash(str):
    def __hash__(self) -> int:
        """
        This is a slightly optimized version of twoletter_hash
        """
        return ord(self[1]) + 26 * ord(self[0]) - 2619


baddict = set()
gooddict = set()

for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        key = i + j
        baddict.add(BadHash(key))
        gooddict.add(GoodHash(key))


badtime = timeit.repeat(
    "key in baddict",
    setup="from __main__ import baddict, BadHash; key = BadHash('zz')",
    repeat=3,
    number=1_000_000
)
goodtime = timeit.repeat(
    "key in gooddict",
    setup="from __main__ import gooddict, GoodHash; key = GoodHash('zz')",
    repeat=3,
    number=1_000_000
)

print(f"Min lookup time for baddict: {min(badtime)}")
print(f"Min lookup time for gooddict: {min(gooddict)}")
