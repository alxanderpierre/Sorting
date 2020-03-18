# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0


    for k in range(0, elements):
        if a >= len(arrA):
            merged_arr[k] = arrB[b]
            b+=1

        elif b >= len(arrB):
            merged_arr[k]= arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            a+=1
        else:
            merged_arr[k] = arrB[b]
            b+=1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) >1:
        left = merge_sort(arr[0 : len(arr) //2])
        right = merge_sort( arr[len(arr) //2:])

        arr = merge(left, right)

    return arr













# this is doing merge sort in one function
def mergeSort( arr ):
  print(f"Slitting, {arr}")
  if len(arr) >1:

    mid = len(arr) //2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    merge_sort(lefthalf)
    merge_sort(righthalf)
    i=j=k=0
    while i < len(lefthalf) and j < len(righthalf):
      if lefthalf[i] < righthalf[j]:
        arr[k] = lefthalf[i]
        i=i+1
      else:
        arr[k] = righthalf[j]
        j=j+1
      k=k+1

    while i < len(lefthalf):
      arr[k] = lefthalf[i]
      i=i+1
      k=k+1

    while j < len(righthalf):
      arr[k] = righthalf[j]
      j=j+1
      k=k+1

    print(f'Merging {arr}')


    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
