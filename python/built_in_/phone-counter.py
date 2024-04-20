import re
from collections import Counter


DB = [
    ('RU', '(495) 123-45-67'),
    ('US', '206-123-4567'),
    ('US', '(206) 123-4567'),
    ('US', '206-123-4567'),
    ('GB', '(020) 1234 5678'),
    ('GB', '020 1234 5678'),
]


def get_pattern(phone):
    '''
    Determine a pattern from a phone number
    '''
    pattern = re.sub(r'\s+', ' ', phone)
    return re.sub(r'\d', '{}', pattern)


def format(pattern, phone):
    '''
    Format `phone` according to `pattern`
    '''
    return pattern.format(*re.findall(r'\d', phone))


def determine_patterns(db):
    '''
    Determine prevalent patterns in an input db

    db: sequence of `(country, phone)`

    Returns a dict `{country: prevalent_pattern}`
    '''
    stats = Counter((country, get_pattern(phone)) for country, phone in db)
    stats = reversed(stats.most_common())
    return {country: pattern for (country, pattern), _ in stats}

if __name__ == '__main__':
    patterns = determine_patterns(DB)
    print('RU', format(patterns['RU'], '1234567890'))
    print('US', format(patterns['US'], '1234567890'))
    print('GB', format(patterns['GB'], '01234567890'))
