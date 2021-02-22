def swap(array, left, right):
    print(f"swapping {array[left]} {array[right]}...")
    temp = array[left]
    array[left] = array[right]
    array[right] = temp
    print(array)


def selectionSort(array):
    sorted_ptr = 0

    while sorted_ptr < len(array) - 1:
        smallest_ptr = sorted_ptr
        for i in range(sorted_ptr + 1, len(array)):
            if array[i] < array[smallest_ptr]:
                smallest_ptr = i

        swap(array, sorted_ptr, smallest_ptr)

        sorted_ptr += 1

    return array