def parse_int(string):
    digits = {
            'zero': 0,
            'nought': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9
        }

    tenth_digits = {
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'dozen': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19
        }

    tenths = {
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90
        }

    multipliers = {
            'hundred': 100,
            'thousand': 1_000,
            'million': 1_000_000,
            'billion': 1_000_000_000,
            'quadrillion': 1_000_000_000_000
        }

    result = 0
    # prepare = re.split(r"\s+|-", string)
    prepare = string.split()
    length = len(prepare)

    prepare.remove('and')
    prepare.append('and')

    print('Length: ', len(prepare))
    print('Prepared: ', prepare)
    

    for i in range(0, length, 2):
        target = prepare[i]
        print('Target:', target)
        if target in digits:
            if prepare[i+1] in multipliers:
                result += (digits[target] * multipliers[prepare[i+1]])
            else:
                result += digits[target]

        if target in tenth_digits:
            if prepare[i+1] in multipliers:
                result += (tenth_digits[target] * multipliers[prepare[i+1]])
            else:
                result += tenth_digits[target]

        if target in tenths:
            if prepare[i+1] in multipliers:
                result += (tenths[target] * multipliers[prepare[i+1]])
            else:
                result += tenths[target]

        if '-' in target:
            el = target.split('-')
            if prepare[i+1] in multipliers:
                result += (tenths[el[0]] + digits[el[1]]) * multipliers[prepare[i+1]]
            else:
                result += (tenths[el[0]] + digits[el[1]])

        # if target in keywords:
        #     continue



    # for i, target in enumerate(prepare):
    #     # print(target)
    #     if target in digits:
    #         result += digits[target]
    #         print(result)
    #     elif target in tenth_digits:
    #         result += tenth_digits[target]
    #         print(result)
    #     elif target in tenths:
    #         result += tenths[target]
    #         print(result)
    #     elif target in multipliers:
    #         result *= multipliers[target]
    #         print(result)
    #     elif target in keywords:
    #         # print(target)
    #         continue
    #     else:
    #         print()
    #         el = target.split('-')
    #         print('With dash: ', el)
    #         result += (tenths[el[0]] + digits[el[1]])
    #         print('So: ', result)
    #         print()


    print()
    print('Current result: ', result)
    print('Final result should be: 783919')
    # return result


# 165
# text = 'one hundred sixty-five'

# 783919
text2 = 'seven hundred eighty-three thousand nine hundred and nineteen'


# print(parse_int(text))
parse_int(text2)
# print(parse_int(text2))
















# 783919
# 'seven hundred eighty-three thousand nine hundred and nineteen'

# Steps

# | words    | digits    | comment |
# |----------+-----------+---------|
# | seven    | 7         |         |
# | hundred  | 700       | 00      |
# | eighty   | 780       | 80      |
# | three    | 783       | 3       |
# | thousand | 783000    | 000     |
# | nine     | 7830009   | 9       |
# | hundred  | 783000900 | 00      |
# | and      | -         | -       |
# | nineteen | 783000919 | 19      |

