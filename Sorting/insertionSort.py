import io
from typing import List
""" algo

- Start with the second element (the first element is considered sorted).
- Compare the current element with the elements in the sorted portion (to its left).
- Shift all larger elements to the right to make space for the current element.
- Insert the current element into its correct position.
- Repeat the process for all elements in the array.
"""

def insertion_sort(arr: List) -> List:
    arr = list(arr)
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
        
    return arr


unsorted_arr = [83, 27, 54, 68, 92, 39, 74, 
                15, 61, 46, 58, 87, 99, 32, 
                70, 43, 66, 95, 25, 51, 79, 
                11, 86, 31, 48, 72, 90, 55, 
                64, 12, 37, 77, 63, 19, 82, 
                50, 29, 96, 40, 67, 22, 71, 
                89, 33, 53, 98, 45, 84, 59, 26]
sorted_arr = insertion_sort(unsorted_arr)
print(unsorted_arr)
print(sorted_arr)