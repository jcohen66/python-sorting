"""
Demonstrates IIFE - Immediately Invoked Function Execution
"""

def product(x, y):
    return x * y

from functools_demo import reduce

sequences = [1,2,3,4,5]
product = reduce(lambda x,y: product(x,y), sequences)
print(product)