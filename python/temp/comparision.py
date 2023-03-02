def compare(str):
    if str.find('<') == 1:
        result = str.split('<')
        return result[0] < result[1]
    else:
        result = str.split('>')
        return result[0] > result[1]


print(compare('2>5'))
print(compare('7<5'))
print(compare('1<5'))
print(compare('1>5'))
