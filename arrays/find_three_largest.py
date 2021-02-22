def findThreeLargestNumbers(array):
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num)

    return three_largest

def update_largest(three_largest, num):
    '''
    >>> l = [None, None, None]
    >>> update_largest(l, 100)
    [None, None, 100]
    >>> l = [4, 99, 123]
    >>> update_largest(l, 100)
    [99, 100, 123]
    >>> l = [99, 100, 123]
    >>> update_largest(l, 541)
    [100, 123, 541]
    '''
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)
    return three_largest

def shift_and_update(array, num, idx):
    '''
    replace the value at the given index
    with the given value
    else shift the value to the right.

    >>> l = [1,2,3]
    >>> shift_and_update(l, 4, 0)
    [4, 2, 3]
    >>> l = [1,2,3]
    >>> shift_and_update(l, 4, 1)
    [2, 4, 3]
    >>> l = [1,2,3]
    >>> shift_and_update(l, 4, 2)
    [2, 3, 4]
    >>> l = [1,2,3]
    >>> shift_and_update(l, 4, 3)
    [1, 2, 3]
    '''
    # bad index passed
    if idx > len(array)-1:
        return array

    for i in range(idx + 1):
        if i == idx:
            # raplace value
            array[i] = num
        else:
            # Shift value left
            # Leftmost value drops off
            array[i] = array[i + 1]
    return array