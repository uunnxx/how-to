def scramble(s1, s2):
    for i in s2:
        if i in s1:
            s1 = s1.replace(i, '', 1)
        else:
            return False
    return True


print('Should be True: ', scramble('rkqodlw', 'world'))

# False
print('Should be False: ', scramble('iyrhogljxpicu', 'xuuihjr'))

# False
print('Should be False: ', scramble('cosspedswyoxrrvh', 'sserrosywdro'))
