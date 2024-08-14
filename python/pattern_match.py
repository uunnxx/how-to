def pattern_match(pattern: str, string: str) -> bool:
    def backtrack(pattern, string, dic):
        lpattern = len(pattern)
        lstring = len(string)
        if (lpattern == 0) and (lstring > 0):
            return False

        if lpattern == lstring == 0:
            return True

        for end in range(1, lstring - lpattern + 2):
            if pattern[0] not in dic and string[:end] not in dic.values():
                dic[pattern[0]] = string[:end]
                if backtrack(pattern[1:], string[end:], dic):
                    return True

                del dic[pattern[0]]
            elif pattern[0] in dic and dic[pattern[0]] == string[:end]:
                if backtrack(pattern[1:], string[end:], dic):
                    return True

        return False
    return backtrack(pattern, string, {})


p = 'abab'
s = 'redblueredblue'

# p = 'aabb'
# s = 'somethingsome'

print(pattern_match(p, s))
