# TO-DO: Complete the selection_sort() function below
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

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    return arr
