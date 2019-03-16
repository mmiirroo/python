def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if(smallest > arr[i]):
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = [] ##declare
    for i in range(0, len(arr)): ##range
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index)) ##pop
    return newArr

print selectionSort([9,8,7,5,10,1])
