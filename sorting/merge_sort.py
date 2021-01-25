"""
Stable Sort.
Good for large lists.

Break the list into two halves, sort those halves recursively
using merge sort, then merge the halves together again.
Relies on the fact that merging two sorted lists is O(n)
operation which is fast.

BigO: O(n log n)

Needs to allocate extra space.
"""

import random
import time
from timed_func import timed_func


def merge_sorted_lists(left, right):
    # Use floating pointers in each list
    left_index, right_index = 0, 0
    return_list = []

    while len(return_list) < len(left) + len(right):
        left_item = left[left_index] if left_index < len(left) else float('inf')
        right_item = right[right_index] if right_index < len(right) else float('inf')
        if left_item < right_item:  #Choose the smallest remaining item and add to list
            return_list.append(left_item)
            left_index += 1
        else:
            return_list.append(right_item)
            right_index += 1
    return return_list


def merge_sort(items):
    # Cant get better than size=1
    if len(items) <= 1:
        return items

    midpoint = len(items) // 2
    # slice the list into two left and right lists at the midpoint
    left, right = items[:midpoint], items[midpoint:]
    # Recursive calls for left abd right lists
    return merge_sorted_lists(merge_sort(left), merge_sort(right))





items = [5, 3, 1, 4, 2]
print(items)
print(merge_sort(items))

items = [1, 2, 5, 2, 3, 8, 1]
print(items)
print(merge_sort(items))

items = [random.randint(1, 1000) for _ in range(100000)]
print(items)
start = time.perf_counter()
print(merge_sort(items))
print(time.perf_counter() - start)