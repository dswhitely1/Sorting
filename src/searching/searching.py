# STRETCH: implement Linear Search				
def linear_search(arr, target):
    # TO-DO: add missing code
    for index, item in enumerate(arr):
        if item == target:
            return index

    return -1
    # return -1  # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1
    # TO-DO: add missing code
    found = False
    while low <= high and not found:
        middle = low + high // 2
        print(middle)
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
        return -1  # array empty
    middle = (low + high) // 2

    if low > high:
        return -1
    elif arr[middle] < target:
        return binary_search_recursive(arr, target, middle + 1, high)
    elif arr[middle] > target:
        return binary_search_recursive(arr, target, low, middle - 1)
    else:
        return middle

# TO-DO: add missing if/else statements, recursive calls
