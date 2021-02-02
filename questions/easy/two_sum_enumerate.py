def two_sum(nums, target):
    '''
    Given an array of integers and a target
    integer, return an array containing the
    indexes of the elements that add up to
    the target.
    >>> two_sum([2,7,11,15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]
    >>> two_sum([3,3], 6)
    [0,1]
    '''
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]
