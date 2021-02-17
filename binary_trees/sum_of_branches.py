class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    arr = []
    branchSumsR(root, 0, arr)
    return arr


def branchSumsR(root, s, arr):
    # Write your code here.
    if root is None:
        return

    new_running_sum = s + root.value
    if root.left is None and root.right is None:
        arr.append(new_running_sum)
        return

    branchSumsR(root.left, new_running_sum, arr)
    branchSumsR(root.right, new_running_sum, arr)
