def threeNumberSum(array, targetSum):
    array = sorted(array)
    result = []
    for curr_idx in range(len(array) - 1):
        left = curr_idx + 1
        right = len(array) - 1

        while left < right:
            val = array[curr_idx] + array[left] + array[right]
            if targetSum == val:
                # add triplet to result
                result.append([array[curr_idx], array[left], array[right]])
                left += 1
                right -= 1

            elif val < targetSum:
                # move left ptr
                left += 1
            else:
                right -= 1

    return result