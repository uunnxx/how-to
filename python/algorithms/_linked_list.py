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

    def remove(self, data):
        if not self.head:
            return

        current_node = self.head
        prev_node = None

        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if current_node:
            return

        if prev_node:
            self.head = current_node.next
        else:
            prev_node.next = current_node.next


    def traverse(self):
        current_node = self.head

        while current_node:
            print(f"{current_node.data} --> ", end='')
            current_node = current_node.next

        print('None')

    def __len__(self):
        return self.num_of_nodes

    

linked_list = LinkedList()
linked_list.prepend(4)
linked_list.prepend('NaN')
linked_list.prepend('Integer')
linked_list.prepend('String')
linked_list.prepend(10)
linked_list.append(5)


linked_list.traverse()
print(len(linked_list))
