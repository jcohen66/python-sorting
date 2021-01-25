lst = [1, 2, -5, 4]

def square(x):
    return x * x


list(map(square, lst))

# >>> [1, 4, 25, 16]

result = []
for num in lst:
    result.append(square(num))

# >>> [1, 4, 25, 16]

# List comprehension
[square(num) for num in lst]

# >>> [1, 4, 25, 16]


# Filter
def is_odd(x):
    return x % 2 == 1


list(filter(is_odd, lst))

# >>> [1, -5]

[num for num in lst if is_odd(num)]

# >>> [1, -5]

grid0 = [[0,0,0],
         [0,0,0]]
print(grid0)

num_rows = 2
num_columns = 3

grid = []
for _ in range(num_rows):
    curr_row = []
    for _ in range(num_columns):
        curr_row.append(0)
    grid.append(curr_row)

print(grid)

# For comprehension
grid = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
print(grid)

