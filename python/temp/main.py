SYN_MAP = {
    'yandex.ru': 'ya.ru',
    'protonmail.com': 'pm.me'
}


def normalize(email: str) -> str:
    if email.count('@') == 1:
        email = email.strip().lower()
        address, domain = email.split('@')

        if domain in SYN_MAP:
            return f"{address}@{SYN_MAP[domain]}"

        return email

    return 'Incorrect email!'


m = 'Yandexoid@yandex.ru'
n = 'Yan@dexoid@protonmail.com'
t = 'yandex@yandex.ru'
p = 'yandex@yandex-team.ru'

print(normalize(m))
print(normalize(n))
print(normalize(t))
print(normalize(p))
# assert normalize(m) == 'yandexoid@ya.ru'
