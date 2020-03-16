# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 




        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # loop through your array
    for i in range(len(arr)-1):
        # compare each element to its neighbor
        for k in range(len(arr)-i-1):
            # If elements in wrong position swap them If no swaps
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
