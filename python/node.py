# Implementing Python Tree Data Structure
# Creating a class for node object

class Node(object):
    # Initializing to None
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


# Inserting a node in Binary search tree
def insertion(val):
    # Condition if this is a first node then it will be considered as a root
    if root.data == None:
        print(val, ' Inserted as root')
        root.data = val
    # Else part will be executed for all the other insertions
    else:
        p = root

        # Creating a new node and writing a value in the data part
        n = Node()
        n.data = val
