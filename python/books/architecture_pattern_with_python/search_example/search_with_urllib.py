import json
from urllib.request import urlopen
from urllib.parse import urlencode

URI = 'http://api.duckduckgo.com'
params = dict(q='Sausage', format='json')
handle = urlopen(f'{URI}?{urlencode(params)}')
raw_text = handle.read().decode('utf8')
parsed = json.loads(raw_text)


results = parsed['RelatedTopics']
for r in results:
    if 'Text' in r:
        print(f"{r['FirstURL']} - {r['Text']}")

