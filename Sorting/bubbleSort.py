import io
from typing import List

def bubble_sort(arr:List) -> List :
    arr = list(arr)
    n = len(arr)
    for c in range(n):
        swapped = False
        for i in range(0, n-c-1):
            if arr[i] > arr[i+1]:
                swapped = True
                arr[i],arr[i+1] = arr[i+1], arr[i]
            if swapped is False:
                break
    return arr

unsorted_arr = [83, 27, 54, 68, 92, 39, 74, 
                15, 61, 46, 58, 87, 99, 32, 
                70, 43, 66, 95, 25, 51, 79, 
                11, 86, 31, 48, 72, 90, 55, 
                64, 12, 37, 77, 63, 19, 82, 
                50, 29, 96, 40, 67, 22, 71, 
                89, 33, 53, 98, 45, 84, 59, 26]

sorted_arr = bubble_sort(unsorted_arr)
print(unsorted_arr)
print(sorted_arr)