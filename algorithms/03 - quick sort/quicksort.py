marks = [12, 23, 65, 98, 32, 45, 78, 87, 65, 12, 56, 21, 45, 23, 45]


class QuickSort:

    def sort(list1):
        QuickSort.quicksort(list1, 0, len(list1)-1)

    def quicksort(list1, left, right):
        if left >= right:
            return
        pivot = list1[(left+right)//2]

        index = QuickSort.partition(list1, left, right, pivot)
        QuickSort.quicksort(list1, left, index-1)
        QuickSort.quicksort(list1, index, right)

    def partition(list1, left, right, pivot):

        while left <= right:
            while (list1[left] < pivot):
                left += 1
            while (list1[right] > pivot):
                right -= 1

            if left <= right:
                QuickSort.swap(list1, left, right)
                left += 1
                right -= 1

        return left

    def swap(array, left, right):
        temp = array[right]
        array[right] = array[left]
        array[left] = temp


QuickSort.sort(marks)

print(marks)
