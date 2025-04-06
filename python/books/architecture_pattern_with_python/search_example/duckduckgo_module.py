import duckduckgo


for r in duckduckgo.query('Sausage').results:
    print(f"{r['FirstURL']} - {r['Text']}")
