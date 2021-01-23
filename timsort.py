"""
Good on both small and large lists.
Block Merge algorithm.

Divide lists into small sections and use insertion sort to sort
all of those sections.  Then merge those sections together two
at a time until the whole list is sorted.

Leverages the strengths of insertions and merge sorts while
mitigating the weaknesses.

BigO: O(n log n)
"""
import random
import time

from insertion_sort import insertion_sort
from merge_sort import merge_sorted_lists
from timed_func import timed_func

@timed_func
def timsort(items):
    min_subsection_size = 32

    for i in range(0, len(items), min_subsection_size):
        insertion_sort(items, i, min((i + min_subsection_size-1), len(items)-1))

    size = min_subsection_size
    while size < len(items):
        for start in range(0, len(items), size * 2):
            midpoint = start + size - 1
            end = min(start + size * 2 - 1, len(items) - 1)

            merged_array = merge_sorted_lists(
                items[start:midpoint + 1],
                items[midpoint + 1: end + 1])

            items[start:start + len(merged_array)] = merged_array
        size *= 2

    return items


items = [5, 3, 1, 4, 2]
print(items)
print(timsort(items))

items = [1, 2, 5, 2, 3, 8, 1]
print(items)
print(timsort(items))

items = [random.randint(1, 1000) for _ in range(1000000)]
print(timsort(items))
