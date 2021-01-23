"""
Stable Sort.
Good for small lists.

Starting at the second element of the list, move each
item so that it;s sorted with respect to all elements
before it.
Inserts each element into its correct place in a sorted
sublist that grows to become the full list.

BigO: n^2
"""

import random
from timed_func import timed_func


#@timed_func
def insertion_sort(items, left=0, right=None):
    """
    Works on a whole list (default) or subsection.

    :param items:   the whole list
    :param left:    start of the subsection
    :param right:   end of the subsection
    :return:
    """
    if right is None:
        right = len(items)-1

    # Traverse second element of subsection
    # all the way through to the end of the
    # subsection
    for i in range(left + 1, right + 1):
        # Get the current item
        current_item = items[i]
        # pointer
        j = i - 1

        # Iterate until you hit beginning of list or the correct point for current item
        while (j >= left and current_item < items[j]):  # Break when current element is in right place
            items[j + 1] = items[j] # move this item up
            j -= 1

        items[j + 1] = current_item # insert current item into its correct spot.

    return items

items = [5,3,1,4,2]
print(items)
print(insertion_sort(items))

items = [1,2,5,2,3,8,1]
print(items)
print(insertion_sort(items))

items = [random.randint(1, 1000) for _ in range(10000)]
print(items)
print(insertion_sort(items))