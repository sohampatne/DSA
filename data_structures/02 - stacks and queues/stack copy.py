class Node:
    def __init__(self, data):
        self.data = data
        self.top = None


class Stack:

    top = None

    def isEmpty(self):
        if self.top:
            return False
        else:
            return True

    def peek(self):
        return self.top.data

    def push(self, data):
        newNode = Node(data)

        newNode.next = self.top
        self.top = newNode

        return newNode

    def pop(self):
        x = self.top
        self.top = self.top.next
        return x
