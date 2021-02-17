def nonConstructibleChange(coins):
    '''
    >>> nonConstructibleChange([5,7,1,1,2,3,22])
    20
    >>> nonConstructibleChange([1,1])
    3
    >>> nonConstructibleChange([1,1,2,4])
    9
    '''

    # Write your code here.
    # sort the values
    coins = sorted(coins)
    current_change_created = 0
    for coin in coins:
        if coin > current_change_created + 1:
            # We know we cant create the current + 1 so return it.
            return current_change_created + 1

        # Accumulate
        current_change_created += coin

    # dropped thru so done
    return current_change_created + 1