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


'''
For simplicity, consider the data in the range 0 to 9. 
Input data: 1, 4, 1, 2, 7, 5, 2
  1) Take a count array to store the count of each unique object.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  2  0  1  1  0  1  0  0

  2) Modify the count array such that each element at each index 
  stores the sum of previous counts. 
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  4  4  5  6  6  7  7  7

The modified count array indicates the position of each object in 
the output sequence.
 
  3) Output each object from the input sequence followed by 
  decreasing its count by 1.
  Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 2.
  Put data 1 at index 2 in output. Decrease count by 1 to place 
  next data 1 at an index 1 smaller than this index.
'''


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    print(f'Input: {arr}')
    # Need to define a count list with a maximum passed in, maybe the max of the array
    # Modify the count array to add sums of the previous indexes
    count_list = [0 for x in range(0, maximum)]
    # Loop through the range 0 - maximum
    # Search Arr for all numbers in the index
    # Add the total to count[index]
    for i in range(0, maximum):
        total = 0
        for y in range(0, len(arr)):
            if arr[y] == i:
                total += 1
        count_list[i] = total

    # Need a positional counter to hold change position
    # While Loop while sum of count_list > 0

    current_index = 0
    list_index = 0
    while current_index < maximum:
        if count_list[current_index] > 0:
            arr[list_index] = current_index
            count_list[current_index] -= 1
            list_index += 1
        else:
            current_index += 1
    return arr


print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
print(count_sort([4, 8, 4, 2, 0, 0, 6, 2, 9], 10))
