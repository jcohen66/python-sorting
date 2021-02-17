'''
Get a list of branch sums from left to right
in a BST.  Use depth first traversal.
'''

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    '''
    Driver with starting values for root node,
    zero sum for the start value of the first
    branch and empty array for the branch sums.
    :param root:
    :return:
    '''
    arr = []
    branchSumsR(root, 0, arr)
    return arr


def branchSumsR(root, s, arr):
    '''
    Recursive depth-first traversal must take
    everything it needs with it in each call.

    :param root:    Current node
    :param s:       Sum of values for the branch
    :param arr:     Array of completed branch sums
    :return:
    '''
    # Bounce off the bottom.
    if root is None:
        return

    # Update the running total with the current node value.
    new_running_sum = s + root.value
    # If current node is a leaf then add
    # the sum to the array and return.
    if root.left is None and root.right is None:
        arr.append(new_running_sum)
        return

    # Recurse left passing everything we need.
    branchSumsR(root.left, new_running_sum, arr)
    # Recurse right passing everything we need.
    branchSumsR(root.right, new_running_sum, arr)

# Driver
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
# root.right.left = BinaryTree(4)
# root.right.right = BinaryTree(5)
# root.right.right.left = BinaryTree(6)
# root.right.right.right = BinaryTree(7)

print(branchSums(root))