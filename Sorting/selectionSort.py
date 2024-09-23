import io
from typing import List

"""algo

- Start with an empty sorted section and the full unsorted list.
- Find the **minimum element** in the unsorted section.
- Swap the minimum element with the first element of the unsorted section.
- Repeat the process for the rest of the unsorted section, reducing its size by one in each iteration.
"""

def selection_sort(arr: List) -> List:
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


unsorted_arr = [83, 27, 54, 68, 92, 39, 74, 
                15, 61, 46, 58, 87, 99, 32, 
                70, 43, 66, 95, 25, 51, 79, 
                11, 86, 31, 48, 72, 90, 55, 
                64, 12, 37, 77, 63, 19, 82, 
                50, 29, 96, 40, 67, 22, 71, 
                89, 33, 53, 98, 45, 84, 59, 26]
sorted_arr = selection_sort(unsorted_arr)
print(unsorted_arr)
print(sorted_arr)