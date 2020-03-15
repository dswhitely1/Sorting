# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # print(f'Element at current index, {arr[cur_index]} - Smallest Element, {arr[smallest_index]}')
        for y in range(cur_index + 1, len(arr)):
            if arr[y] < arr[smallest_index]:
                # print('*** Before ***')
                # print(f'{arr[smallest_index]} - {arr[y]}')
                temp_number = arr[smallest_index]
                arr[smallest_index] = arr[y]
                arr[y] = temp_number
                # print('*** After ***')
                # print(f'{arr[smallest_index]} - {arr[y]}')
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap_occurred = True
    while swap_occurred:
        swap_occurred = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp_number = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp_number
                swap_occurred = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr


print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
