def count_dups(L):
    '''
    Given an array of chars, return an
    array of the counts of consecutive
    chars.
    >>> count_dups([1, 1, 1, 2, 2, 3])
    [3, 2, 1]
    >>> count_dups([5, 5, 5, 5, 2, 2, 2, 3, 3, 3])
    [4, 3, 3]
    >>> count_dups([])
    []
    >>> count_dups([1])
    [1]
    '''
    ans = []
    if not L:
        return ans

    running_count = 1
    # range minue last char to accomodate two ptrs i and i+1.
    for i in range(len(L) - 1):
        if L[i] == L[i + 1]:
            running_count += 1
        else:
            ans.append(running_count)
            running_count = 1
    ans.append(running_count)
    return ans