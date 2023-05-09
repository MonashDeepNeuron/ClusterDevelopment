def insertionSort(array):
    # start at index 1
    for i in range(1,len(array)):
    # iterate through the array, each time the next element is the key
        key = array[i]
    # initialise j element left of the current key
        j = i -1
    # while key is < than elements to on left, move all elements > key right by one 
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
         # j to point to the next element
            j -= 1

    # then move key to its correct new position after the element just smaller than it.
        array[j+1]=key