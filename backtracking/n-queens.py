'''
You have an N by N board. Write a function that
returns the number of possible arrangements of
the board where N queens can be placed on the
board without threatening each other, i.e. no
two queens share the same row, column, or diagonal.
'''


def n_queens(n, board=[]):
    '''
    Represent the board as 1D array of 1..N integers.
    The value at index i is the column the queen on that
    row i is on.
    Since we are working incrementally, we don't even need
    to have the whole board initialized.  We can just
    append and pop as we go down the stack.
    :param n:       The column to try the queen
    :param board:   1D array representing the row
    :return:
    '''
    if n == len(board):
        return 1

    count = 0
    for col in range(n):
        # Add the col to the board as an incremental change
        # to attempt.
        board.append(col)
        if is_valid(board):
            # Recurse with the incremental change to the board
            # and the queen in the new position.
            count += n_queens(n, board)
        # it didnt work so backtrack by removing
        # the incremental change.
        board.pop()
    return count

def is_valid(board):
    '''
    Check the board on each incremental addition.  Look at
    the last queen placed and see if any other queen can threaten
    it.
    If so, then prune the branch since there's no point pursuing it.
    Otherhwise, recursively call ourselves with the new incremental
    soluton.
    We can stop once we hit the base case: we've placed all the
    queens on the board already.
    :param board:
    :return:
    '''
    current_queen_row, current_queen_col = len(board) -1, board[-1]
    # Check if any queens can attack the last queen.
    for row, col in enumerate(board[:-1]):
        diff = abs(current_queen_col - col)
        if diff == 0 or diff == current_queen_row - row:
            return False
    return True

# Loop thru and place queen in col n.
for i in range(10):
    print(n_queens(i))