class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def is_identical(x, y):
    """
    Recursive function to check it two given binary
    trees are identical.
    """

    # if both trees are empty, return true
    if x is None and y is None:
        return True

    # if both trees are non-empty and the value of
    # the root nodes match then recurse for the
    # left and right subtrees.
    return (x and y) and \
           (x.key == y.key) and \
            is_identical(x.left, y.left) and \
           is_identical(x.right, y.right)

if __name__ == '__main__':
    # construct the first tree
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(16)
    x.right.right = Node(25)

    # construct the first tree
    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)
    y.left.left = Node(81)
    y.left.right = Node(12)
    y.right.left = Node(16)
    y.right.right = Node(25)

    if is_identical(x, y):
        print("The given binary trees are identical.")
    else:
        print("The given binary trees are NOT identical.")


