def isMonotonic(array):
    is_nonIncreasing = True
    is_nonDecreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            is_nonDecreasing = False
        if array[i] > array[i - 1]:
            is_nonIncreasing = False

    return is_nonDecreasing or is_nonIncreasing
