def walk_perimeter(array, result, start_row, start_col, end_row, end_col):
    # keep row same, increate col until reach col count

    # top border
    for col in range(start_col, end_col + 1):
        result.append(array[start_row][col])

    # right side border
    for row in range(start_row + 1, end_row + 1):
        result.append(array[row][end_col])

    # bottom border
    for col in range(end_col - 1, start_col - 1, -1):
        # edge case for single row
        if start_row == end_row:
            break
        result.append(array[end_row][col])

    # left side border
    for row in range(end_row - 1, start_row, -1):
        # edge case for single column
        if start_col == end_col:
            break
        result.append(array[row][start_col])

    return result


def spiralTraverse(array):
    # create an empty result array
    result = []

    start_row = 0
    start_col = 0
    end_row = len(array) - 1
    end_col = len(array[0]) - 1

    while start_row <= end_row and start_col <= end_col:
        walk_perimeter(array, result, start_row, start_col, end_row, end_col)
        start_row += 1
        start_col += 1
        end_row -= 1
        end_col -= 1

    return result