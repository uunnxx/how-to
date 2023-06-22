from pprint import pprint as print


obj = {
    'car': 'BMW',
    'age': 18,
    'hoddy': 'Football'
}


for k, v in obj.items():
    print(f"{k} --> {v}")
