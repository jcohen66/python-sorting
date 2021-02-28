def arrayOfProducts(array):
    '''
    >>> arrayOfProducts([5, 1, 4, 2])
    [8, 40, 10, 20]
    '''
    products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        products[i] *= left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        products[i] *= right_running_product
        right_running_product *= array[i]

    return products
