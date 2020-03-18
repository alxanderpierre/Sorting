# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
  print(f"Slitting, {nlist}")
  if len(nlist) >1:

    mid = len(nlist) //2
    lefthalf = nlist[:mid]
    righthalf = nlist[mid:]

    merge_sort(lefthalf)
    merge_sort(righthalf)
    i=j=k=0
    while i < len(lefthalf) and j < len(righthalf):
      if lefthalf[i] < righthalf[j]:
        nlist[k] = lefthalf[i]
        i=i+1
      else:
        nlist[k] = righthalf[j]
        j=j+1
      k=k+1

    while i < len(lefthalf):
      nlist[k] = lefthalf[i]
      i=i+1
      k=k+1

    while j < len(righthalf):
      nlist[k] = righthalf[j]
      j=j+1
      k=k+1

    print(f'Merging {nlist}')


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
