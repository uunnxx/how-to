from create_apartment import Apartment


d1 = Apartment(_id=1, mts2=100, value=5000)

print(f"sold? {d1.sold}")
d1.sell()

print(f"sold? {d1.sold}")
d1.sell()


