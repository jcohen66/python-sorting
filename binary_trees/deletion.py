"""
Given a binary tree, delete a node from it by making sure that the tree
shrinks from the bottom ie deleted node is replaced by the deepest and
rightmose node.
This is different from a BST since there is no sort order.
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)

def delete_deepest(root, d_node):
    """
    delete the given deepest node (d_node) in the binary tree.
    """
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return

        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)

        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

def deletion(root, key):
    # 1) Starting at root, find the deepest and rightmost node and node we want to delete.
    # 2) Replace the deepest rightmost node's data with the node to be deleted.
    # 3) Delete the deepest rightmost node.

    if root == None:
        return None

    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root

    key_node = None
    q = []
    q.append(root)

    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if key_node:
        x = temp.data
        delete_deepest(root, temp)
        key_node.data = x
    return root

# Driver
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    """
            10
         11     9
       7   12 15  8         
    """

    print("The tree before the deletion: ")
    inorder(root)

    key = 11
    root = deletion(root, key)

    print("The tree after the deletion: ")
    inorder(root)