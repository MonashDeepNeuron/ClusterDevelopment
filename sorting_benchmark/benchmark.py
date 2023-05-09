import random
import time
import pandas as pd
import numpy as np
import sorting_benchmark.bubble as bubble
import merge
import counting
import insertion
import quick

import matplotlib.pyplot as plt

# runs the benchmarking,
def benchmarking(algorithms, Sizes, runs):
    # create some variables to append the output to
    elapsed_times = [] # this should end up with 10 elapsed times for each innermost loop
    input_size =[] # to record the array size used for each run
    trials =[] # to record the current trial number for each algorithm
    type =[] #  to record the name of the sorting algorithm used


    # for each of the 5 sorting algorithms 
    for sort_algo in algorithms:
        print(f"running {sort_algo}")        
        # for each array size in the size array
        for size in Sizes:
            # run this 10 (runs) times for each size for each sort type
            for run in range(runs):
                # generate random arrays
                x = [random.randint(0,100) for i in range(size)]

                #print(f" function {sort_algo} on array of length {len(x)}")
                # select the sorting algorithm to use
                algorithm = algorithms[sort_algo]
                # time.time return the time in seconds since the epoch as a floating point number
                start_time = time.time()
                # run the actual algorithm on the current run on the current array size
                algorithm(x)
                end_time = time.time()
                time_elapsed = (end_time - start_time)* 1000 # to get milliseconds

                # record the results of current test to the results array
                elapsed_times.append(time_elapsed)               
                # record the current run number (from 1 to 10)
                trials.append(run+1)
                # record the current size to the input size array
                input_size.append(size)
                # record the name of the current sorting algorithm 
                type.append(sort_algo) 

    # outputs a dataframe with the raw times for each trial              
    df = pd.DataFrame({"Sort":type, "Size":input_size, "Times":elapsed_times, "trialNo":trials})
    return df

# Define a function to take the output of the benchmarking function and calculate the averages 
def mean_sorts(df):
    # use the Size column of the dataframe as the index
    df.set_index('Size', inplace=True)
    # calculate the averages for each sorting algorithm at each level of input size
    means = (df.iloc[:, 0:2].groupby(['Sort','Size']).mean()).round(3)
    # unstack the dataframe to get the desired format for the output to the console
    return means.unstack()

# define a function to plot the averages on a graph
def plot_averages(df2):
    # import plotting libraries
    import seaborn as sns
    import matplotlib.pyplot as plt
    # set the plot paramters
    plt.rcParams["figure.figsize"]=(16,8)
    sns.set(style= "darkgrid")
    # transpose the dataframe for plotting
    df2.T.plot(lw=2, colormap='jet', marker='.', markersize=10, 
         title='Benchmarking Sorting Algorithms - Average Times')
    plt.ylabel("Running time (milliseconds)")
    plt.xlabel("Input Size")
    #plt.ylim(0,80)
    #plt.show()
    # save image
    plt.savefig('plot100.png', bbox_inches='tight')

# define a function to export the results to csv
def export_results(times, means):
    # change this to store in a different file each time so I can compare results
    times.to_csv('xxxTime_trials' + '100'+'.csv')
    means.to_csv('xxxAverages' + '100' + '.csv')

# call the main program
if __name__ == "__main__":
    # the list of algorithms to be used
    algorithms = {"BubbleSort": bubble.bubbleSort,"insertionSort":insertion.insertionSort,"mergeSort":merge.merge_sort, "quickSort":quick.quickSort, "CountingSort": counting.CountingSort}
    # provide the sizes for the arrays to be sorted    
    sizeN = [250,500,1000]
    sizeN = [100,250,500,750,1000,1250,2500]

    # call the benchmarking function
    results = benchmarking(algorithms, sizeN, 5)

    print("The running time for each of the 5 sorting algorithms have been measured 10 times and the averages of the 10 runs for each algorithm and each input size are as follows \n ")
    # create a dataframe to store the averages resulting from the benchmarking
    df2=  mean_sorts(results)
    # drop 'Sort'
    df2.rename_axis(None, inplace=True)
    # drop one of the multi-index levels
    df2.columns = df2.columns.droplevel()
    # print the results to the console
    print(df2)
    # call the plotting function
    plot_averages(df2)
    # export the results to csv
    export_results(results, df2)