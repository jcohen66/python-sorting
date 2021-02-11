class Node(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        '''
        Finds the place in the tree and inserts the given data.
        '''
        # Does root exist?
        if self.data:
            if data < self.data:
                # left subtree
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                # right subtree
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

            # Print the Tree

    def PrintTree(self):
        '''
        Inorder traversal - recursive
        '''
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self, root):
        '''
        # Inorder traversal - recursive with list
        # Left -> Root -> Right
        '''
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

# Driver
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(22)
root.PrintTree()
print(root.inorderTraversal(root))

'''
                27
        14              35
    10      19      31      22
'''