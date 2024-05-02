def scoreboard(who_ate_what):
    output = []
    for dicts in who_ate_what:
        values = dicts.values()
        names = [name for name in values if isinstance(name, str)]
        scores = [i for i in values if isinstance(i, int)]
        output = [{'name': name, 'score': sum(scores)} for name in names]

        print(output)




# output = [
#   {'name': "Big Bob", 'score': 134},
#   {'name': "Habanero Hillary", 'score': 98}
# ]

# scoreboard(inp)


def scoreboard2(who_ate_what):
    result = []
    name = ''
    scores = []
    total_score = []

    for dicts in who_ate_what:
        items = dicts.items()
        for values in items:
            match values[0]:
                case 'name':
                    name = values[1]
                case 'chickenwings':
                    scores.append(values[1] * 5)
                case 'hamburgers':
                    scores.append(values[1] * 3)
                case 'hotdogs':
                    scores.append(values[1] * 2)
                case _:
                    scores.append(values[1])

        result.append({'name': name, 'score': sum(scores)})
        total_score += scores
        scores = []

    if sum(total_score) % len(total_score) == 0:
        return sorted(result, key=lambda dicts: dicts['name'])

    return sorted(result, key=lambda dicts: dicts['score'], reverse=True)



inp0 = [{'name': "Habanero Hillary", 'chickenwings': 5 , 'hamburgers': 17, 'hotdogs': 11}, {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}]
inp2 = [{'name': 'Billy The Beast', 'score': 122}, {'name': 'Habanero Hillary', 'score': 98}, {'name': 'Joey Jaws', 'score': 94}, {'name': 'Big Bob', 'score': 134}]
inp3 = [{'name': 'Dr. Peter Silberman', 'score': 134}, {'name': 'Kyle Reese', 'score': 53}, {'name': 'Skynet', 'score': 150}, {'name': 'T1000', 'score': 70}, {'name': 'T800', 'score': 12}]
inp4 = [{'name': 'Dr. Peter Silberman', 'score': 41}, {'name': 'John Connor', 'score': 41}, {'name': 'Kyle Reese', 'score': 100}, {'name': 'Miles Bennett Dyson', 'score': 25}, {'name': 'Sarah Connor', 'score': 54}, {'name': 'Skynet', 'score': 138}, {'name': 'T-X', 'score': 165}, {'name': 'T1000', 'score': 0}]
inp5 = [{'name': 'T-X', 'score': 165}, {'name': 'Skynet', 'score': 138}, {'name': 'Kyle Reese', 'score': 100}, {'name': 'Sarah Connor', 'score': 54}, {'name': 'Dr. Peter Silberman', 'score': 41}, {'name': 'John Connor', 'score': 41}, {'name': 'Miles Bennett Dyson', 'score': 25}, {'name': 'T1000', 'score': 0}]

# inp6 = [{'name': 'Big Bob', 'score': 22}]
# inp6_answer = [{'name': 'Big Bob', 'score': 134}]



inp7 = [{'name': 'Joey Jaws', 'score': 5}, {'name': 'Big Bob', 'score': 5}]
inp7_answer = [{'name': 'Big Bob', 'score': 5}, {'name': 'Joey Jaws', 'score': 5}]


assert scoreboard2(inp7) == inp7_answer
print(scoreboard2(inp7))






