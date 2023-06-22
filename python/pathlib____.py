from pathlib import Path


# some_string = "I'm here?"
#
# res = []

# for i in some_string:
#     lower = i.lower()
#     if i == ' ':
#         res.append(' ')
#     elif i.lower() == i.upper():
#         continue
#     else:
#         res.append(i.lower())


# print(''.join(res))


print(Path.cwd())
print(f"{Path(__file__).absolute()}/cookies.txt")
