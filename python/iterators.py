# The Iterator pattern is a behavioral design pattern that allows us to traverse the elements of a collection without exposing the underlying data structure. In Python, we can use the built-in iter() and next() functions to implement the Iterator pattern. Here's an example implementation of the Iterator pattern in Python:


class MyCollection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return MyIterator(self._items)

class MyIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

# Using the iterator
collection = MyCollection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")


for item in collection:
    print(item)




# In the above example, we first define a MyCollection class that represents a collection of items. The MyCollection class has a _items list that holds the items, and an add_item method that adds an item to the list.

# We also define an __iter__ method in the MyCollection class that returns a new MyIterator object. This allows us to use the built-in iter() function on the collection object.

# We then define a MyIterator class that represents an iterator over the collection. The MyIterator class has a _items list and an _index variable that keep track of the current position in the list.

# The MyIterator class also has an __iter__ method that returns itself, and a __next__ method that returns the next item in the list, or raises a StopIteration exception when there are no more items.

# Finally, we create a MyCollection object and add some items to it. We then use a for loop to iterate over the items in the collection using the MyIterator object.

# The output of the above code will be:



# >> Item 1
# >> Item 2
# >> Item 3


# This shows that we can use the Iterator pattern in Python to traverse the elements of a collection without exposing its underlying data structure. By implementing the Iterator pattern, we can separate the collection traversal logic from the collection implementation, and make our code more flexible and reusable.


