
# TO-DO: Complete the selection_sort() function below


from collections import defaultdict


def selection_sort(arr):
    # loop through n-1 elements
    length = len(arr)
    while length > 0:
        largest = arr[0]
        largest_index = 0
        for i in range(0, length):
            if arr[i] > largest:
                largest = arr[i]
                largest_index = i
            if i == length-1:
                arr[largest_index] = arr[i]
                arr[i] = largest
        length -= 1
        # cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    length = len(arr)
    changes = True
    while length > 0 and changes == True:
        changes = False
        for i in range(0, length-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                changes = True
        length -= 1

    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr):
    # Your code here
    count = defaultdict(int)
    # arrays length of 1 and less our sorted
    if len(arr) <= 1:
        return arr
    # maximum value in array (pretend not given)
    k = 0
    # tally all values in dictionary
    for i in arr:
        count[i] += 1
        if i > k:
            k = i
    # create a new array with length of k+1
    setup = [0] * (k+1)
    # runner tells us what all numbers prior =
    runner = 0
    # loop thru all values of k in dictionary and insert into list
    for j in range(k+1):
        runner += count[j]
        setup[j] = runner
    # create the final array which will return a sorted array
    final = [0] * len(arr)
    # lastly loop thru arr 1 last time find index in setup by decrement 1 and set final[index] to arr[i]
    for i in range(len(arr)):
        setup[arr[i]] -= 1
        index = setup[arr[i]]
        final[index] = arr[i]

    return final


print(count_sort([1]))
print(count_sort([2]))
print(count_sort([1, 2, 3, 4, 5]))
print(count_sort([1, 2, 1, 3, 2, 1, 5, 4, 2, 3, 1, 0, 0, 0, 0]))
