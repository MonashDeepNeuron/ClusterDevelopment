def bubbleSort(array):
    # loop n-1 times

    for passnum in range(len(array)-1,0,-1):
        # inner loop is shorted by 1 each time as another element is sorted
        for i in range(passnum): 
            # comparing each element i with the element right beside it (i+1)  
            if array[i] > array[i+1] : 
                # swap out of order pairs so largest element is right of the smaller one
                array[i], array[i+1] = array[i+1], array[i]