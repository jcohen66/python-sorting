'''
Calculate the numbet of ways/steps to solve a problem.

You are climbing a stair case.  You can take either
1 or 2 steps at a time.  How many ways are there to
the top?
'''

def num_ways(n):
    '''
    Just like fibonacci sequence, use recursion.
    Not efficient bc calculations are repeated.
    >>> num_ways(4)
    5
    '''
    if n == 0 or n == 1:
        return 1

    return num_ways(n-1) + num_ways(n-2)

def num_ways_bottom_up(n):
    '''
    Solve how many ways using dynamic programming.
    >>> num_ways_bottom_up(4)
    5
    '''
    # Base case:  Just 1 way to climb 0 or 1 stairs.
    if n == 0 or n == 1:
        return 1

    # allocate array for solution
    dp = []
    for i in range(n+1):
        dp.append(0)

    # Solve to 0 and 1 steps
    dp[0] = 1
    dp[1] = 1

    # Solve for 2 upto n+1 steps
    for i in range(2, n+1):
        # Can only take 1 or 2 steps at a time...
        # Where could you have come from? only i-1 and i-2.
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]