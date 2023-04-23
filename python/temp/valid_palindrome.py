# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

string = 'radkar'


def solution(given):
    print(f"{given=}")
    for i in range(len(given)):
        check = given[:i] + given[i+1:]
        print(f"{check=} {i=}")
        print(f"{given[:i]=} {given[i+1:]=}")
        print(f"{'-' * 40}\n")

        # if check == t[::-1]: return True

    return given == given[::-1]


solution(string)
