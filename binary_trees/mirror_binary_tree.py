class TreeNode(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder(root):
    if not root:
        return

    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)


def mirror(root):
    if not root:
        return

    mirror(root.left)
    mirror(root.right)

    if root.left and root.right:
        temp = root.left
        root.left = root.right
        root.right = temp

# Driver
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

preorder(root)
print()
mirror(root)
preorder(root)