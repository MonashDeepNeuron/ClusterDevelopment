def quickSort(array):
    # call a recursive function that takes in the array, 
    quickSortHelper(array,0,len(array)-1)
    return array

# if length of list passed in is > 1, partition the array and recursively sort
def quickSortHelper(array,first,last):
    if first<last:
        splitpoint = partition(array,first,last)  # find the split point
        # recursively call the function on the two halves of the array
        quickSortHelper(array,first,splitpoint-1)
        quickSortHelper(array,splitpoint+1,last)

# a function to partition the array using the pivot element, 
def partition(array,first,last):
    # the pivot is the first element in the array
    pivotvalue = array[first]
    # the first pointer is the first element in the remaining unsorted part
    leftmark = first+1
    # the right pointer is the last element remaining 
    rightmark = last

    done = False
    while not done:
        # move the first pointer right until the first element > pivot is found
        while leftmark <= rightmark and array[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        # move the second pointer left until the first element < pivot 
        while array[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        # stop when the second pointer is less than the first pointer (when cross over) 
        if rightmark < leftmark:
            done = True
        else:
           # using simulataneous assignment to swap the values that are out of place
            array[leftmark],array[rightmark]  = array[rightmark], array[leftmark]
    # swap with the pivot value 
    array[first],array[rightmark] = array[rightmark],array[first]

    return rightmark