import re


def get_pattern(phone):
    pattern = re.sub(r'\s+', ' ', phone)  # normalize whitespace
    return re.sub(r'\d', '{}', pattern)   # replace digits with plaaceholders


def format(pattern, phone):
    return pattern.format(*re.findall(r'\d', phone))


{
    'US': {
        '({}{}{}) {}{}{}-{}{}{}{}': 1,
        '{}{}{}-{}{}{}-{}{}{}{}': 2
    },
    'GB': {
        '{}{}{} {}{}{} {}{}{}{}': 1
    },
    'RU': {
        '({}{}{}) {}{}{}-{}{}-{}{}': 1
    }
}


from collections import defaultdict


stats = defaultdict(lambda: defaultdict(int))  # nested defaultdicts

for country, phone in DB:
    pattern = get_pattern(phone)
    stats[country][pattern] += 1

# Replace eeach country stats with teh most common pattern
for country, patterns in stats.items():
    pattern = max(patterns.items(), key=lambda i: i[1])[0]
    stats[country] = pattern


# Counter
from collections import defaultdict, Counter


stats = defaultdict(Counter)

for country, phone in DB:
    pattern = get_pattern(phone)
    stats[country][pattern] += 1

for country, patterns in stats.items():
    # most_common would return a list [(pattern, count)], so we need [0][0] here
    stats[country] = patterns.most_common(1)[0][0]



# Flat and functional
from collections import Counter


def determine_patterns(db):
    stats = Counter((country, get_pattern(phone)) for country, phone in db)
    stats = reversed(stats.most_common())
    return {country: pattern for (country, pattern), _ in stats}



