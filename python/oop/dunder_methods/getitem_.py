import os
from PIL import Image


L = [10, 20, 30, 40, 50]

print(L[0])  #  => 10


class ShoppingList:
    def __init__(self):
        self.items: list[str] = ['Apple', 'Banana', 'Milk', 'Carrot']


# shopping_list = ShoppingList()
# print(shopping_list[0])  # => __getitem__ method not defined
# print(shopping_list.items[0])

# for item in shopping_list:  # object is not iterable
#     print(item)

class ShoppingList1:
    def __init__(self):
        self.items: list[str] = ['Apple', 'Banana', 'Milk', 'Carrot']

    def __getitem__(self, idx: int):
        return self.items[idx]

    def __len__(self):
        return len(self.items)


shopping_list = ShoppingList1()

print(shopping_list[0])
print()

for item in shopping_list:
    print(item)


if 'Milk' in shopping_list:
    print('You have to buy milk')


print(len(shopping_list))



class ImageDataset:
    root: str

    def __init__(self, root: str) -> None:
        self.root = root
        self.filenames: list[str] = os.listdir(self.root)

    def __getitem__(self, idx: int):
        # return self.filenames[idx]
        img = Image.open(self.root + '/' + self.filenames[idx])
        return img

    def __len__(self):
        return len(self.filenames)


