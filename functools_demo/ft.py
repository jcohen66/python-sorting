from functools_demo import reduce

result = reduce(lambda x,y: x * y, [1,2,3,4], 10)

print(result)