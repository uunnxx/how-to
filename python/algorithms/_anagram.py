def is_anagram(str1, str2):
    length = len(str1)
    if length != len(str2):
        return False

    # sorted is O(n log n)
    str1 = sorted(str1)
    str2 = sorted(str2)

    # O(n)
    for ch in range(length):
        if str1[ch] != str2[ch]:
            return False

    # O(n log n) + O(n) => O(n log n)
    return True


if __name__ == '__main__':
    s1 = 'fluster'
    s2 = 'restful'

    print(is_anagram(s1, s2))
