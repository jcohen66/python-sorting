def count_unique(s):
    '''
    Count number of unique characters in s
    >>> count_unique("aabb")
    2
    >>> count_unique("abcdef")
    6

    :param s:
    :return:
    '''
    seen_c = []                 # O(1)
    for c in s:                 # O(n) *
        if c not in seen_c:     # O(n) *
            seen_c.append(c)    # O(1)
    return len(seen_c)          # O(n^2)

def count_unique_set(s):
    '''
    Count number of unique characters in s
    >>> count_unique_set("aabb")
    2
    >>> count_unique_set("abcdef")
    6
    '''
    seen_c = set()          # O(1)
    for c in s:             # O(n) *
        if c not in seen_c: # O(1)
            seen_c.add(c)   # O(1)
    return len(seen_c)      # O(n)


def count_unique_set_comprehension(s):
    '''
    Count number of unique characters in s
    >>> count_unique_set_comprehension("aabb")
    2
    >>> count_unique_set_comprehension("abcdef")
    6
    '''

    return len({c for c in s})

def count_unique_set_comprehension_iterable(s):
    '''
    Count number of unique characters in s
    >>> count_unique_set_comprehension_iterable("aabb")
    2
    >>> count_unique_set_comprehension_iterable("abcdef")
    6
    '''

    return len(set(s))  # O(n)