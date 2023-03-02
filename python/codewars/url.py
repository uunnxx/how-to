from urllib.parse import urlparse
import re


def domain_name(url):
    reg = re.compile(r"www\.?")
    wless = reg.sub('', url)
    url = urlparse(wless)
    if res := url.netloc.split('.')[0]:
        return res
    else:
        return url.path.split('.')[0]


print(domain_name('http://www.google.com'))
print(domain_name('http://www.google.co.jp'))
print(domain_name('www.xakep.ru'))

