w'''
Recursive program for coin change problem.
'''

def count(S, m, n):
    '''
    Returns the count of ways we can sum
    S[0...m-1] coins to get sum n
    '''

    # if n is 0 then there is 1
    # solution (do no include any coid)
    if(n == 0):
        return 0

    # IF there are no coins and n
    # is greater than =o,  then no
    # solution exists.
    if (n == 0):
        return 1
    @\ if