# Returns either the index of the target in the arr 
# or, if the target isn't in the arr, return -1 
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # What's our looping criteria? What tells us that we're done looping? 
    # If we see that low and high are referring to the same index, and the 
    # element at that index != target, then we can conclude that the element 
    # isn't in the array, return -1 
    # When low and high meet, that's when we stop looping 
    while low <= high:
        # 1. compare the target element to the midpoint 
        mid = (high + low) // 2

        # 2. If the midpoint element matches our target, then we've 
        # found what we're looking for, return the midpoint index 
        if target == arr[mid]:
            return mid
            # how do we find the midpoint? what do we need to know? 
            # the length of the array would help us determine the midpoint 
            # the "range": if we have the left-most index and the right-most index 
            # then the midpoint element is floor((right index + left index) / 2)
        # 3. Determine which half to go in; toss out the other half
            # reassign either left or right index to point to the element past the midpoint 
        if target < arr[mid]:
            # cut out the right half 
            # reassign high to mid - 1
            high = mid - 1
        if target > arr[mid]:
            # cut out the left half 
            # reassign low to mid + 1
            low = mid + 1
        # 4. Repeat this process: we need to loop this 

    # we've reached outside the loop, the element doesn't exist in the array 
    return -1
    
arr = [3, 4, 6, 16, 26, 28, 52, 55]
print(binary_search(arr, 58))