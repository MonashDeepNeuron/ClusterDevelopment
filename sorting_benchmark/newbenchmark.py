import random
import time
import bubble
import merge
import counting
import insertion
import quick



def benchmark(functions, size, runs):
    time_taken =[]*len(functions)
    unsorted_array= [random.randint(0,100000) for i in range(size)]

    for function in functions:
        array = unsorted_array.copy()
        start_time = time.time()
        function(array)
        end_time = time.time()
        time_elapsed = (end_time - start_time)* 1000 # to get milliseconds
        time_taken.append(time_elapsed)
    return time_taken

functions = [bubble.bubbleSort , merge.merge_sort, counting.CountingSort, insertion.insertionSort, quick.quickSort]
sizes =[100, 1000, 10000, 100000, 1000000]
for size in sizes:

    res = benchmark(functions, size, 10)
    f = open("benchmark.txt", "a")
    f.write(f"size: {size}\nbubbleSort: {res[0]}, merge_sort: {res[1]}, CountingSort: {res[2]}, insertionSort: {res[3]}, quickSort: {res[4]}\n")
    f.close()


    