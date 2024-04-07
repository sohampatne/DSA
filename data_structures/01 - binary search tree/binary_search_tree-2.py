class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, value):

    if (root == None):
        root = Node(value)
    elif (value <= root.data):
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def search(root, value):

    if (root == None):
        return False
    else:
        print(root.data)
    if (value == root.data):
        return True
    elif (value <= root.data):
        return search(root.left, value)
    else:
        return search(root.right, value)


myroot = Node(40)

insert(myroot, 50)
insert(myroot, 30)
insert(myroot, 10)

found = search(myroot, 50)

print(found)
# print(myroot.data)
