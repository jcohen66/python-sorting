from math import floor
from collections import defaultdict

def majority_element_indexes(lst):
    '''
    Return a list of the indexes of the majority element.
    Majoirity element is the element that appears more than
    floor(n/2) times.
    If there is no majority element, return [] (empty list)
    >>> majority_element_indexes([1,1,2])
    [0, 1]
    >>> majority_element_indexes([1,1,2,2,2,2])
    [2, 3, 4, 5]
    >>> majority_element_indexes([1,2])
    []
    >>> majority_element_indexes([])
    []
    '''
    # no me due to lack of elements
    if len(lst) <= 2:
        return []
    # Calculate me
    elems = defaultdict(lambda: 0)
    for x in lst:
        elems[x] += 1
    me = max(elems, key=elems.get)

    # validate me against floor
    flr = floor(len(lst)/2)
    result = []
    if elems[me] <= flr:
        return result

    # Populate the result with the index positions
    for i in range(len(lst)):
        if me == lst[i]:
            result.append(i)
    return result
