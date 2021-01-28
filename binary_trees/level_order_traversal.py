"""
Traverse and print a binary tree
in level order.
"""

class Node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def levelorder(root):
    h = height(root)
    for i in range(1, h+1):
        print_given_level(root, i)

def print_given_level(root, level):
    # Base case
    if root is None:
        return

    if level == 1:
        print(root.key)
    else:
        # print("level", level)
        print_given_level(root.left, level-1)
        print_given_level(root.right, level-1)



def height(node):
    # Base case
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

# Driver
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left.left = Node(10)
root.right.right.right = Node(11)

"""
              1
          2       3
        4   5   6   7
      8  9    10     11
"""

print("Level order traversal of binary tree is -")
levelorder(root)
