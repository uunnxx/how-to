from itertools import zip_longest


def mergeAlternately(word1: str, word2: str) -> str:
    st = []
    for i, j in zip_longest(word1, word2):
        st.extend([i, j])
    return ''.join(list(filter(bool, st)))
    


a = mergeAlternately('abc', 'pqr')
b = mergeAlternately('ab', 'pqrs')

print(a)
print(b)


assert a == 'apbqcr'
assert b == 'apbqrs'



def findTheDifference(s: str, t: str) -> str:
    s, t = set(s), set(t)
    if len(t) == 1:
        return ''.join(t)
    return ''.join(t ^ s)


print(findTheDifference('a', 'aa'))


aa = ['a', 'e']
ab = ['a', 'e', 'a']


print(aa - ab)
