def palindrome(string: str) -> bool:
    from re import sub
    string = sub('[\W_]', '', string.lower())
    return string == string[::-1]


print(palindrome('cat,) tac'))
