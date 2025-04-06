import requests


URI = 'http://api.duckduckgo.com'
params = dict(q='Sausage', format='json')
parsed = requests.get(URI, params=params).json()

results = parsed['RelatedTopics']
for r in results:
    if 'Text' in r:
        print(f"{r['FirstURL']} - {r['Text']}")

