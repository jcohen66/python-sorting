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

def preorder(root):
    if root is None:
        return

    print(root.key, end=' ')
    preorder(root.left)
    preorder(root.right)


def swap(root):
    """
    Swap the left and right subtrees using
    an temporary node.
    """
    temp = root.left
    root.left = root.right
    root.right = temp

def convert_to_mirror(root):
    # base case: root is None
    if root is None:
        return

    # convert left subtree
    convert_to_mirror(root.left)

    # convert right subtree
    convert_to_mirror(root.right)

    # swap left and right subtrees
    swap(root)

if __name__ == '__main__':
    # construct the first tree
    x = Node(1)
    x.left = Node(2)
    x.right = Node(3)
    x.left.left = Node(4)
    x.left.right = Node(5)
    x.right.left = Node(6)
    x.right.right = Node(7)

    """
                  1
                2   3
               4 5 6 7
    """

    preorder(x)
    convert_to_mirror(x)
    print()
    preorder(x)


