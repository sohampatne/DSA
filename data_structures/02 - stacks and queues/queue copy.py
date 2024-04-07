class Node:
    def __init__(self, data):
        self.data = data
        self.top = None


class Queue:

    head = None  # remove
    tail = None  # add

    def isEmpty(self):
        if self.top:
            return False
        else:
            return True

    def peek(self):
        return self.top.data

    def push(self, data):
        newNode = Node(data)

        self.tail.next = newNode
        newNode = self.tail

        return newNode

    def pop(self):
        x = self.head
        self.head = self.head.next
        return x
