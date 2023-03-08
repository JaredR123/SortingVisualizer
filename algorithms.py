array = [2, 1, 7, 8, 6, 5, 11, 31, 25, 36, 37, 0, 9, 13]
array1 = [5, 4, 3, 2, 1, 0]
ascending = False

def bubble_sort(array, ascending):
    sort_length = len(array) - 1

    for i in range(sort_length):
        # The largest value not already sorted will be sorted by the end of the next iteration of
        # i, so after i iterations we need to sort through i less values, thus "sort_length - i"
        for j in range(0, sort_length - i): 
            if (array[j] > array[j + 1] and ascending or array[j] < array[j + 1] and not ascending):
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

def selection_sort(array, ascending):
    for i in range(len(array)):
        min_position = i

        for j in range(i, len(array)):
            if (array[min_position] > array[j] and ascending or array[min_position] < array[j] and not ascending):
                min_position = j
        
        array[i], array[min_position] = array[min_position], array[i]

    return array
        

print(selection_sort(array1, ascending))