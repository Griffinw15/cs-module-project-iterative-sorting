# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        smallest_val = arr[cur_index]

        # TO-DO: swap
        # Your code here
        for unsorted_index in range(cur_index, len(arr)):
            if arr[unsorted_index] < smallest_val:
                smallest_val = arr[unsorted_index]
                smallest_index = unsorted_index

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

#def selection_sort(items):
#    # Outer Loop
#    for i in range(0, len(items) - 1):
#        cur_index = i
#        smallest_index = cur_index
#        for j in range(cur_index + 1, len(items)):
#            if items[j] < items[smallest_index]:
#                smallest_index = j
#
#        items[smallest_index], items[cur_index] = items[cur_index], items[smallest_index]
#
#    return items

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    #make length variable
    n = len(arr)
    # loop through n-1 elements
    for i in range(n-1):
        #i value is already there, another -1 bc of the pairs in bubbling
        #traverse from 0 to last pair
        for x in range(0, n-i-1):
            #if left is bigger than right, switch
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here

    return arr
