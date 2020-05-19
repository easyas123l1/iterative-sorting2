def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    high = len(arr)-1
    low = 0
    while high >= low:
        middle = (high + low) // 2
        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
