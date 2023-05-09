def CountingSort(array):
    n= len(array)
    # a counter array initialised with zeros, 
    counter= [0 for i in range(max(array)+1)]
    sorted = []   #to store the sorted values
    # loop over elements, use the element of input as the index for the counter 
    for i in array:
        # each time an element appears in the array, increment the counter by 1
        counter[i] += 1
    # Use count of each element occurs to place elements in the sorted array

    for i in range(0,len(counter)):
        # while the counter shows that there is a matching element
        while counter[i] > 0:
            # append the element to the sorted array
            sorted.append(i)
           # decrease the counter by 1 each time
            counter[i] -= 1
    return sorted