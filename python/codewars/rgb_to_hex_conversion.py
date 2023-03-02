def rgb(r, g, b):
    # return ''.join([format(hx, '02X') if hx <= 255 else 'FF' for hx in [r, g, b]])

    rgbs = []
    for i in [r, g, b]:
        if i > 255:
            rgbs.append(255)
        elif i < 0:
            rgbs.append(0)
        else:
            rgbs.append(i)

    return ''.join([format(hx, '02X') for hx in rgbs])


print(rgb(255, 255, 300))   # returns FFFFFF
print(rgb(0,0,0))           # returns 000000
print(rgb(148, 0, 211))     # returns 9400D3
print(rgb(0, 0, 0))         # "000000", "testing zero values")
print(rgb(1, 2, 3))         # "010203", "testing near zero values")
print(rgb(255, 255, 255))   # "FFFFFF", "testing max values")
print(rgb(254, 253, 252))   # "FEFDFC", "testing near max values")
print(rgb(-20, 275, 125))   # "00FF7D", "testing out of range values")
