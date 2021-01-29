"""
Solve for a solution path to the rat maze
using a backtracking algo.
"""

# Dimensions of maze
N = 4

def print_solution(solution_path):
    for i in solution_path:
        for j in i:
            print(str(j) + " ", end="")
        print("")

def is_safe(maze, x,y):
    """
    Check if position is in-bounds and is part of solution.
    """
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False

def solve_maze(maze):
    """
    Use solveMazeUtil to determine of there is a path
    otherwise return false.
    """
    solution_path = [ [ 0 for j in range(4)] for i in range(4) ]

    if solve_maze_util(maze, 0, 0, solution_path) == False:
        print("Solution doesn't exist")
        return False

    print_solution(solution_path)

def solve_maze_util(maze, x, y, solution_path):
    # if x,y is goal return True
    if x == N-1 and y == N-1 and maze[x][y] == 1:
        solution_path[x][y] = 1
        return True

    # Check if maze[x][y] is valid
    if is_safe(maze, x, y):
        # mark x, y as part of solution path
        solution_path[x][y] = 1

        # Move forward in x direction
        if solve_maze_util(maze, x + 1, y, solution_path) == True:
            return True

        # If moving in x direction doesn't give solution
        # then move down in y direction
        if solve_maze_util(maze, x, y + 1, solution_path) == True:
            return True

        # If none of the above movements work then
        # BACKTRACK: unmark x, y as part of solution path
        solution_path[x][y] = 0
        return False

# Driver
if __name__ == '__main__':

    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]

solve_maze(maze)
