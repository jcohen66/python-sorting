"""
Insert a node into a binary tree.

Do iterative level order traversal of the given tree using a queue.
If we find a node whose left child is empty, make a new key as left child of node.
Else if we find a node whose right child is empty, make a new key as right child of node.
Keep traversing the tree until we find a node whose either left or right child is empty.
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    """
    Inorder traversal of a binary tree
    """
    if not root:
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)

def insert(root, key):
    if not root:
        return

    q = []
    q.append(root)

    # Do level order traversal until we find
    # an empty place.
    while (len(q)):
        root = q[0]
        q.pop(0)

        if (not root.left):
            root.left = Node(key)
        else:
            q.append(root.left)

        if (not root.right):
            root.right = Node(key)
        else:
            q.append(root.right)

# Driver code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before insertion: ", end = " ")
    inorder(root)

    key = 12
    insert(root, key)

    print()
    print("Inorder traversal before insertion: ", end = " ")
    inorder(root)