from random import randint


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def prepend(self, data):
        self.num_of_nodes += 1
        node = Node(data)

        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def append(self, data):
        self.num_of_nodes += 1
        node = Node(data)
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def traverse(self):
        current_node = self.head

        while current_node:
            print(f"{current_node.data} --> ", end='')
            current_node = current_node.next

        print('None')

    def __len__(self):
        return self.num_of_nodes


range_of = 20
n = [randint(i, range_of) for i in range(range_of)]

linked_list = LinkedList()
for num in n:
    linked_list.prepend(num)

linked_list.traverse()
print(len(linked_list))
