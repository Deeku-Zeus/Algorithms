import io
from typing import List

unsorted = [2,5,4,1,8,6,9,3,7]

def bubble_sort(unsorted: List[int]) -> List:
    sorted = unsorted
    for start in range(0, len(unsorted)):
        for end in range(start+1, len(unsorted)):
            if unsorted[start] > unsorted[end]:
                sorted[start], sorted[end] = sorted[end], sorted[start]
    return sorted

sorted = bubble_sort(unsorted = unsorted)
print(sorted)