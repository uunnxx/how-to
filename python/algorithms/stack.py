class Stack:
    def __init__(self):
        self.items: list[str | int] = []
        self._max: list[int] = []
        self._min: list[int] = []

    def push(self, item: str | int):
        self.items.append(item)

        if item > self.max():
            self._max.append(item)
        else:
            self._max.append(self._max[-1])

    def max(self):
        if self._max:
            return self._max[-1]
        return None

    def min(self):
        if self._min:
            return self._min[-1]
        return None

    @property
    def is_empty(self):
        return self.items == []

    @property
    def pop(self) -> str | int:
        return self.items.pop()

    @property
    def peek(self) -> str | int:
        return self.items[len(self.items)-1]

    @property
    def size(self) -> int:
        return len(self.items)


stack = Stack()
stack.push('Red')
stack.push('Green')
stack.push('Blue')
stack.push('Yellow')
stack.push('Orange')


print(stack.peek)
print(stack.pop)
print(stack.peek)
print(stack.size)
print(stack.pop)
print(stack.peek)
print(stack.size)
stack.push('Magenta')
print(stack.peek)
