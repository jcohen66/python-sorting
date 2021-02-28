def longestPeak(array):
    lptr = 0
    mptr = 0
    rptr = 0
    max_count = 0

    # edge case min array size
    if len(array) == 3:
        if array[0] < array[1] > array[2]:
            return 3
        else:
            return 0

    for i in range(1, len(array) - 1):
        lptr = i - 1
        mptr = i
        rptr = i + 1

        # Identify peak
        if array[lptr] < array[mptr] > array[rptr]:

            # scan left from mptr - 1 and guard falling off beginning
            count = 3
            ptr = mptr - 1
            while ptr > 0 and array[ptr - 1] < array[ptr]:
                count += 1
                ptr -= 1

            # scan right and guard falling off end
            ptr = mptr + 1
            while ptr < len(array) - 1 and array[ptr] > array[ptr + 1]:
                count += 1
                ptr += 1

            # take only the highest
            max_count = max(count, max_count)

    return max_count