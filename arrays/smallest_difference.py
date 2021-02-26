def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallest_pair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        first_num = arrayOne[idxOne]
        second_num = arrayTwo[idxTwo]
        if first_num < second_num:
            current = second_num - first_num
            idxOne += 1
        elif second_num < first_num:
            current = first_num - second_num
            idxTwo += 1
        else:
            return [first_num, second_num]

        if smallest > current:
            smallest_pair = [first_num, second_num]
            smallest = current

    return smallest_pair
