def isMonotonic(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            # update direction
            direction = array[i] - array[i - 1]
            continue
        if breaks_direction(direction, array[i - 1], array[i]):
            return False

    return True


def breaks_direction(direction, previous_int, current_int):
    difference = current_int - previous_int
    if direction > 0:
        return difference < 0
    return difference > 0