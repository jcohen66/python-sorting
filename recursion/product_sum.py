def productSum(array, multiplier=1):
    '''
    Multiplier stats at 1 so numbers can
    be summed at top level as is.

    Recursion takes care of increasing the
    multiplier as the subproblem gets called
    multiple times.
    '''
    sum = 0
    for element in array:
        # detect the next nested special element
        if type(element) is list:
            # Each time through the multiplier goes up
            sum += productSum(element, multiplier + 1)
        else:
            # Just sum the numbers
            sum += element
    # multiply the sum of the subproblem by the multiplier
    return sum * multiplier
