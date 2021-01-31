"""
Possible moves:
(x-1, y-1)
(x-1, 0)
(x-1, y+1)
(x, y-1)
(x, y+1)
(x+1, y-1)
(x+1, y)
(x+1,y+1)
"""

# Lists detail all 8 possible movements from a cell.
# (top, right, bottom, left and 4 diagonal moves)
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0,  1, -1, 1, -1, 0, 1]

def is_safe(x, y, processed):
    """
    Check if its safe to move to cell(x,y) from current cell.
    Returns false if (x,y) is not valid or if cell has
    already been processed.
    """
    return (0 <= x <= M) and \
           (0 <= y <= N) and \
           not processed[x][y]

def search_boggle(board, words, processed, i, j, path=""):
    """
    Recursive function to generate all possible words in a boggle.
    """

    # mark current node as processed
    processed [i][j] = True

    # update the path with the current character and
    # insert it into the set.
    path = path + board[i][j]
    words.add(path)

    # Check for all 8 possible movements from the current cell.
    for k in range(8):
        # skip if cell is invalid or it is already processed
        if is_safe(i + row[k], j + col[k], processed):
            search_boggle(board, words, processed, i + row[k], j + row[k], path)

    # mark current node as unprocessed
    processed[i][j] = False


def search_in_boggle(board, input):
    """
    Search for a given set of words in aboggle
    """

    # construct a matrix to store whether a cell is processed or not.
    processed = [[False for x in range(N)] for y in range(M)]

    # construct a set to store all possible words
    # constructed from the matrix.
    words = set()

    # generate all possible words in boggle
    for i in range(M):
        for j in range(N):
            # consider each character as a starting point and run its DFS
            search_boggle(board, words, processed, i, j)

    # for each word in the input list, check whether
    # it is present in the set.

# Driver
if __name__ == '__main__':
    board = [
        ['M', 'S', 'E'],
        ['R', 'A', 'T'],
        ['L', 'O', 'N']
    ]

    (M,N) = (len(board), len(board[0]))

    words = ["STAR", "NOTE", "SAND", "STONE"]
    search_in_boggle(board, words)