class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val


# def insert(root, node):
#     if root is None:
#         root = node
#     else:
#         if root.data > node.data:
#             if root.l_child is None:
#                 root.l_child = node
#             else:
#                 insert(root.l_child, node)
#         else:
#             if root.r_child is None:
#                 root.r_child = node
#             else:
#                 insert(root.r_child, node)
#
#
# def in_order_place(root):
#     if not root:
#         return
#     in_order_place(root.l_child)
#     print(root.data)
#     in_order_place(root.r_child)
#
#
# def pre_order_print(root):
#     if not root:
#         return
#     print(root.data)
#     pre_order_print(root.l_child)
#     pre_order_print(root.r_child)
#

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.val = val


class BinarySearchTree(object):
    def insert(self, root, node):
        if root is None:
            return node
        if root.val < node.val:
            root.r_child = self.insert(root.r_child, node)
        else:
            root.l_child = self.insert(root.l_child, node)

        return root

    def in_order_place(self, root):
        if not root:
            return None
        else:
            self.in_order_place(root.l_child)
            print(root.val)
            self.in_order_place(root.r_child)

    def pre_order_print(self, root):
        if not root:
            return None
        else:
            print(root.val)
            self.pre_order_print(root.l_child)
            self.pre_order_print(root.r_child)

    def post_order_place(self, root):
        if not root:
            return None
        else:
            self.post_order_place(root.l_child)
            self.post_order_place(root.r_child)
            print(root.val)


r = Node(3)
node = BinarySearchTree()
nodeList = [1, 8, 5, 12, 14, 6, 15, 7, 16, 8]

for nd in nodeList:
    node.insert(r, Node(nd))

# print("----------- In Order -----------")
# print(node.in_order_place(r))
# print("----------- Pre Order ----------")
# print(node.pre_order_print(r))
# print("----------- Post Order ---------")
# print(node.post_order_place(r))
