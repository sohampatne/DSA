class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    top = None

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.top.data

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        x = None
        if (self.top != None):
            x = self.top.data
            self.top = self.top.next
        return x


# testing #
stack1 = Stack()
print(stack1.isEmpty())
stack1.push(10)
print(stack1.peek())

stack1.push(40)
print(stack1.peek())

stack1.push(3)
print(stack1.isEmpty())
print(stack1.peek())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
