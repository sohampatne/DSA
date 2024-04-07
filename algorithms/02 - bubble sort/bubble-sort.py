marks = [1, 53, 90, 45, 67, 12, 34, 15]

lastIndex = len(marks)-1

counter = 0
sorted = False
while sorted == False:
    counter += 1
    sorted = True
    for index in range(0, lastIndex):
        if marks[index] > marks[index+1]:
            temp = marks[index+1]
            marks[index+1] = marks[index]
            marks[index] = temp
            sorted = False

print(f'\nno. of times loop has been executed: {counter}\n')

for x in marks:
    print(x)
