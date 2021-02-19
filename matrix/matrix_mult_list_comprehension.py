# x = [[12, 7,3],
#      [4, 5, 6],
#      [7, 8, 9]]

# y = [[5, 8 ,1, 2],
#      [6, 7, 3, 0],
#      [4, 5, 9, 1]]

x = [[0,3,5],
     [5,5,2]]

y = [[3,4],
     [3,-2],
     [4,-2]]

def dot_product(x, y):
    sum = 0
    for i in x:
        for j in y:
            sum += i * j
    return sum

# E x D
# E cols must equal D rows
if len(x[0]) != len(y):
    print('In an ExD matrix mult, E cols must equal D rows')
    exit(-1)

result = [[sum(a*b for a,b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]

for r in result:
    print(r)

yi = y[:]
xi = x[0]
# print(dot_product(xi, yi))
print(yi)