rules = {3: 'Fizz', 5: 'Buzz'}
for i in range(1, 101):
    output = ''.join(repl for val, repl in rules.items() if i % val == 0)
    print(output or i)
