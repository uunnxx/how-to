# 'ab' is short for 'a'ddress 'b'ook

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print('Swaroop\'s address is', ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']

print(f'\nThere are {len(ab)} contacts in the address-book\n')

for name, address in ab.items():
    print(f'Contact {name} at {address}')

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('\nGuido\'s address is', ab['Guido'])
