class Element:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def compare(self, otherElement):
        result = 0
        if self.data > otherElement.data:
            result = -1
        elif self.data < otherElement.data:
            result = 1
        else:  # self.data == otherElement.data
            if ord(self.name[0]) > ord(otherElement.name[0]):
                result = -1
            elif ord(self.name[0]) < ord(otherElement.name[0]):
                result = 1
            else:
                result = 0
                print("Duplicate value detected.")
        return result


class ElementComparator:
    def compare(element1, element2):
        result = 0
        if element1.data > element2.data:
            result = -1
        elif element1.data < element2.data:
            result = 1
        else:  # element1.data == element2.data
            if ord(element1.name[0]) > ord(element2.name[0]):
                result = -1
            elif ord(element1.name[0]) < ord(element2.name[0]):
                result = 1
            else:
                result = 0
                print("Duplicate value detected.")
        return result


elA = Element("Alice", 10)
elB = Element("Bob", 5)
elC = Element("Bob", 4)
result = ElementComparator.compare(elA, elA)
print(result)

result = ElementComparator.compare(elB, elA)
print(result)

result = ElementComparator.compare(elA, elB)
print(result)

result = ElementComparator.compare(elB, elC)
print(result)

result = elB.compare(elC)
print(result)
