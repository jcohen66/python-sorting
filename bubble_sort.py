"""
Stable Sort.

Move the largest item in the list to the end of the list,
then the second-largest to the second-to-last position...
Named because the element in question bubbles to the top
of the list in a series of swaps with adjacent elements.

BigO: n^2

Does not scale well
"""
from timed_func import timed_func
import random


@timed_func
def bubble_sort(items):
    already_sorted = True
    # i is items already considered
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            # swap them if out of order
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j + 1], items[j]
                already_sorted = False
        if already_sorted:
            break
    return items


items = [5,3,1,4,2]
print(items)
print(bubble_sort(items))

items = [1,2,5,2,3,8,1]
print(items)
print(bubble_sort(items))

items = [random.randint(1, 1000) for _ in range(10000)]
print(items)
print(bubble_sort(items))