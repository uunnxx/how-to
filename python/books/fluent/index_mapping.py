# import re
# import sys
#

# """
# Build an index mapping word -> list of occurrences
# """

# WORD_RE = re.compile(r'\w+')
#
# index = {}

# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             # this is ugly; codde like this to make a point
#             occurrences = index.get(word, [])
#             occurrences.append(location)
#             index[word] = occurrences
#
# # display in alphabetical order
# for word in sorted(index, key=str.upper):
#     print(word, index[word])
#

import collections


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key: object) -> bool:
        return str(key) in self.data

    def __setitem__(self, key, item) -> None:
        self.data[str(key)] = item


from types import MappingProxyType


d = {1: 'A'}
d_proxy = MappingProxyType(d)

print(d_proxy)
print(d_proxy[1])
# d_proxy[2] = 'x'
d[2] = 'B'

print(d_proxy)
