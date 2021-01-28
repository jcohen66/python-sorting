class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.key, end=' ')

def height(root):
    # Base case> root is nNone
    if root is None:
        return 0

    # recurse for the left and right subtree
    # and consider maximum depth. (Plus account for root +1)
    return 1 + max(height(root.left), height(root.right))



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

    postorder(x)
    print("The height of the binary three is: {}".format(height(x)))



