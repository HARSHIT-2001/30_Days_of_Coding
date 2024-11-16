# Bubble sort in Ascending order in Python
def bubbleSort_in_asc(arr):
    
  # loop to access each array element one by one
  for i in range(len(arr)):

    # loop to compare array elements
    for j in range(0, len(arr) - i - 1):

      # comparing two adjacent elements
      # you can change > to < to sort in descending order
      if arr[j] > arr[j + 1]:

        # swapping elements if elements are not in the intended order
        temp_arr = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp_arr


# Bubble sort in Descending order in Python
def bubbleSort_in_desc(arr):
  for i in range(len(arr)):

    for j in range(0, len(arr) - i - 1):

      if arr[j] < arr[j + 1]:

        temp_arr = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp_arr


# Driver Code...
# In Ascending
input_data = [-2, 45, 0, 11, -9]
bubbleSort_in_asc(input_data)
print('Sorted Array in Ascending Order:', input_data)

# In Descending
input_data = [-2, 45, 0, 11, -9]
bubbleSort_in_desc(input_data)
print('Sorted Array in Descending Order:', input_data)

