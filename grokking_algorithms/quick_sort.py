def quicksort(array):
    if len(array) < 2 :
        return array
    else:
        pivot = array[0]
        print array

        less = [i for i in array[1:] if i <= pivot]### not array[i]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([10, 5, 3, 8, 2, 9])
