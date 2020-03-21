# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    # Need to check each side of the list to see which element is lower
    # Once one list is empty, extend the rest onto the merged_arr
    # Define index pointers for LHS and RHS, aka arrA and arrB and increment only when that is appended to the array

    index_a = 0
    index_b = 0

    # Need a condition that will break if one of the lists are empty

    while index_a < len(arrA) and index_b < len(arrB):
        # Check to see if A < B
        if arrA[index_a] < arrB[index_b]:
            merged_arr.append(arrA[index_a])
            # Add 1 to the index so that we compare the next element
            index_a += 1
        else:
            # B > A
            merged_arr.append(arrB[index_b])
            # Add 1 to the index so that we compare the next element
            index_b += 1

    # One side is empty, extend the lists to the merged Array
    # Going to extend based on where index_a and index_b
    merged_arr.extend(arrA[index_a:])
    merged_arr.extend(arrB[index_b:])

    print(f'Elements: {elements}, merged_arr: {merged_arr}')
    # Return sorted List
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Base Case --- We want our list to have only 1 element in it
    if len(arr) <= 1:
        return arr

    # Recursion Case We will keeping calling Merge Sort till we reach our Base Case
    # Let's define the divide point by dividing the length of the List by 2 and returning the int value
    point = int(len(arr) / 2)

    # Let's define our 2 sides, called lhs and rhs and call Merge_sort
    lhs = merge_sort(arr[:point])
    rhs = merge_sort(arr[point:])

    # Test Failed when I separated the Merge Sort Call, reflecting guess I wasn't saving the LHS and RHS Variables
    # To Memory
    # Recursively call merge_sort
    # merge_sort(lhs)
    # merge_sort(rhs)

    # Return the Merge Helper
    print(f'LHS: {lhs}, RHS: {rhs}')
    return merge(lhs, rhs)




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


my_list = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(my_list))