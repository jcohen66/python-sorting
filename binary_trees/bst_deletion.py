class Node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.key)
    inorder(root.right)

def insert(node, key):
    """
    Utility function to insert a new node
    with a given key in a BST.
    """
    # if tree is empty, return a new node.
    if node is None:
        return Node(key)

    # otherwise recurse down the tree.
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node


def minValueNode(node):
    """
    Given a non-empty BST,
    return the node with minimum key value.
    Note that the entire tree might not get searched.
    """
    current = node

    # loop down to find the leftmost leaf
    while(current.left is not None):
        currrent = current.left

    return current

def deleteNode(root, key):
    """
    Given a BST and a key,
    delete the key and
    return the new root
    """
    # Base case:
    if root is None:
        return root

    # if the key to be delete
    # is smaller than the root's key
    # then it lies in the left subtree.
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # if the key to be delete
    # is largerer than the root's key
    # then it lies in the right subtree.
    elif key > root.key:
        root.right = deleteNode(root.right, key)

    # if key is same as root's key
    # then this is the node to be
    # deleted.
    else:
        # Node with only one child or no child.
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root

# Driver

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

"""
          50  
    30          70
20     40    60    80
"""

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)

