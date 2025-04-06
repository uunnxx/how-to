```python

class Circle:
    def __init__(self, radius):
        self.radius = radius


c = Circle(5)

# direct access
c.radius  # => 5

c.radius = 10
c.radius  # => 10
```


```python

# Getter and Setter methods

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._radius = value


c = Circle(5)

# Instead of c.radius
c.get_radius()  # 5

# Instead of c.radius = 10
c.set_radius(10)
c.get_radius()  # 10

```


```python

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        if value < 0:
            raise ValueError('radius must be non-negative')
        self._radius = value

    radius = property(fget=get_radius, fset=set_radius)

    # property(fget=None, fset=None, fdel=None, doc=none)
    # fget -- getter function
    # fset -- setter function
    # fdel -- delete function
    # doc  -- string for attribute doc... help(ClassName)
    # i.e.:
    # radius = property(
    #     fget=get_radius,
    #     fset=set_radius,
    #     fdel=del_radius,
    #     doc='radius of the circle'
    # )

    # OR
    # x = property()
    # x.getter(get_x)
    # x.setter(set_x)
    # x.deleter(del_x)

    # I.E.
    # radius = property(get_radius)
    # radius = radius.setter(set_radius)
    # radius = radius.deleter(del_radius)
    





c = Circle(5)
c.radius = 10
c.radius  # 10
```

Or by using `@property` decorator

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def set_radius(self, value):
        if value < 0:
            raise ValueError('radius must be non-negative')
        self._radius = value

    def del_radius(self):
        print('deleting radius')
        del self._radius

    @property
    def radius(self):
        return self._radius

```



```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """
        Docs string should be located in the getter method

        Radius of the circle
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('radius must be non-negative')
        self._radius = value

    @radius.deleter
    def radius(self):
        print('deleting radius')
        del self._radius


```


Adding `area` method:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self.radius ** 2


c = Circle(5)
c.area()


# Replace with property getter
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property 
    def area(self):
        return math.pi * self.radius ** 2


c = Circle(5)
c.area


# Optimizing for cached `area` method when `radius` is not changed so we'll not compute again area of the Circle

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * (self.radius ** 2)
        return self._area

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._area = None  # Invalidate the cache

```
