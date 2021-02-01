
from collections import Counter

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
    >>> majority_element_indexes([4,4,4,1,1,2,2,2,2,4,4])
    []
    >>> majority_element_indexes([6,6,6,1,1,2,6,6,6,])
    [0, 1, 2, 6, 7, 8]
    >>> majority_element_indexes([1,2])
    []
    >>> majority_element_indexes([])
    []
    '''
    # Nothing to do
    if len(lst) == 0:
        return []

    # Build dictionary with corresponding counts
    count  = Counter(lst)
    # Sort them in reverse order so highest is first
    # Sorted takes O(nlogn) to sort
    top_elems = sorted(
        count.keys(),
        key=lambda x: -count[x]
    )
    # Grab the key with highest count which is now at front of list
    maj_elem = top_elems[0]

    # there exists a majority element
    if count[maj_elem] > len(lst) // 2:
        return [
            # List comprehension guarding just the majority elements.
            # List comprehension takes O(n)
            i for i, elem in enumerate(lst) if elem == maj_elem
        ]
    else:
        # Violates number of maj_elems rule so return empty list.
        return []