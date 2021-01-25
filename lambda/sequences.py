"""
Demonstrates IIFE - Imediately Invoked Function Execution
"""

y = (lambda x: x + x)(2)
print(y)

def greater_than_four(x):
    # print("invoking...")
    return x > 4

def mult(x):
    return x * x

sequences = [10,2,8,7,5,3,11,0,1]
# Define the function but dont invoke it until first reference.
filtered_result = filter(lambda x: greater_than_four(x), sequences)
print(sequences)
# Must invoke list() to execute function.
print("invoking now...")
print(list(filtered_result))

mapped_result = map(lambda x: mult(x), sequences)
print(list(mapped_result))

