'''
>>> fact(5)
120
'''
def fact(n):
    # base case
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)