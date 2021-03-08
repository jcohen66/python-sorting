class Node(object):
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

# A utility function to create a new node
def inorder(root):
    if root is not Node:
        inorder(root.left)
        print(root.ley)
        inorder(root.right)

# A utility function to insert a new node
# with a given key in a BST
def insert(node, key):

    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise recerse down the tree
    if key < node.key:
        node.left = insert(node.left, key)
