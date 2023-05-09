def merge_sort(array):

    if len(array)>1:
        # find the middle of the list to get the split point
        mid = len(array)//2
        # left contains the elements from the first half of the list
        left = array[:mid]
        # right contains the elements from the second half of the list
        right = array[mid:]
        # recursively call the function on the first half
        merge_sort(left)
        # recursively call the function on the second half
        merge_sort(right)


        i ,j, k = 0,0,0 # index of the left, right and merged arrays

        while i < len(left) and j < len(right):
       # compare next element, place smaller element next into sorted array

            if left[i] <= right[j]:
                array[k]=left[i]
                # next comparison
                i += 1
            else:
                array[k]=right[j]
                # next comparison
                j += 1
            # after assigning another element to the merged array, increment the index by 1
            k=k+1
        # if no elements left in right array, move any elements in left to merged array
        while i < len(left):
            array[k]=left[i]
            i += 1
            k += 1
        # no elements left in left array, move any elements in right array to merge
        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1
    return array