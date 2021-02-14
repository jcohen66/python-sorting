'''
Backtracking Algorithm:
You have a partial solution (grid with zeros)
You try to extend it
If you arrive at a solution, fine
If not, call yourself recursively
If no solution, you undo (backtrack) and solve again
Finally, return if no solution possible
'''
import numpy as np

grid0 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]

def possible(y, x, n):
    '''
    Utility function to check if its possible
    to place n value sin the given x,y without
    violating any of the rules:
    - Cannot be in same row
    - Cannot be in same column
    - Cannot be in same box
    :param y: column
    :param x: row
    :param n: value
    :return:
    '''
    global grid

    # Check if in same row
    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    # Check if in same column
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    # Check if in same box
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            # Is there a blank?
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        # Put the value there
                        grid[y][x] = n
                        # We have reduced the problem so use recursion
                        solve()
                        # Bad choice so backtrack
                        grid[y][x] = 0

                # We have tried all possibilitiess
                return

    print(np.matrix(grid))
    input("More?")


print(np.matrix(grid))
print()

# print(possible(4, 4, 3))
# print(possible(4, 4, 5))

solve()
