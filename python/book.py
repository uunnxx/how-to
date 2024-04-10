class Author:
    def __init__(self, name: str, age: int, gender: int):
        self.name = name
        self.age = age

        if gender:
            self.gender = 'Male'
        else:
            self.gender = 'Female'

    def __str__(self):
        return f"Name: {self.name}"


class Book:
    def __init__(self, title: str, pages: int, author: Author):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"\"{self.title}\" by {self.author.name}\n\tinfo: {self.pages} pages"


books = [["Fahrenheit 451", 186]]

ray_bradbury = Author("Ray Bradbury", 91, gender=1)
fahrenheit_451 = Book("Fahrenheit 451", pages=186, author=ray_bradbury)

for book in books:
    s = Book(*book, ray_bradbury)
    print(s)

print()

print(ray_bradbury)
print(fahrenheit_451)


