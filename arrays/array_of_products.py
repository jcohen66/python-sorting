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


def arrayOfProducts_2(array):
    products = [1 for _ in range(len(array))]
    left_products = [1 for _ in range(len(array))]
    right_products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        left_products[i] = left_running_product
        left_running_product *= array[i]
        print(f"lrp {left_running_product}")

    right_running_product = 1
    for i in reversed(range(len(array))):
        right_products[i] = right_running_product
        right_running_product *= array[i]
        print(f"rrp {left_running_product}")

    print(f"left {left_products}")
    print(f"right {right_products}")

    for i in range(len(array)):
        products[i] = left_products[i] * right_products[i]

    print(products)
    return products
