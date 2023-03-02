def pig_it(text):
    res = []
    for i in text.split():
        if len(i) > 1 or i.isalpha():
            res.append(i[1::] + i[0] + 'ay')
        else:
            res.append(i)
    return ' '.join(res)


def pig_it2(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


print(pig_it('Pig latin is cool'))  # igPay atinlay siay oolcay
print(pig_it('Hello world !'))      # elloHay orldway !
