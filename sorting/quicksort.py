"""
NOT Stable.


Choose a pivot element, then divide the list into
three sections:
- Elements that are less than pivot element
- Elements that are equal to pivot element
- Elements that are greater than pivot element

Call quicksort recursively on the less-than and
greater than sublists then concatenate all three.

BigO: n^2
"""

import random
import time
from timed_func import timed_func

def quicksort(items):
    if len(items) <= 1:
        return items

    # Choice of pivot matters.  Can blow out stack.
    # pivot = items[0]
    pivot = random.choice(items)

    # Allocate extra space.
    less_than_pivot = [x for x in items if x < pivot]
    equal_to_pivot = [x for x in items if x == pivot]
    greater_than_pivot = [x for x in items if x > pivot]

    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)



items = [5, 3, 1, 4, 2]
print(items)
print(quicksort(items))

items = [1, 2, 5, 2, 3, 8, 1]
print(items)
print(quicksort(items))

items = [random.randint(1, 1000) for _ in range(1000000)]
print(items)
start = time.perf_counter()
print(quicksort(items))
print(time.perf_counter() - start)