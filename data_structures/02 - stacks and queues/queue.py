class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    tail = None  # add here
    head = None  # remove from here

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def add(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def remove(self):
        if self.head != None:
            x = self.head.data
            self.head = self.head.next
            return x
        else:
            return None


queue1 = Queue()
queue1.add(1)
queue1.add(2)
queue1.add(3)
queue1.add(4)
queue1.add(5)
queue1.add(6)
print(queue1.remove())
print(queue1.remove())
print(queue1.remove())
print(queue1.remove())
print(queue1.remove())
print(queue1.remove())
print(queue1.remove())
