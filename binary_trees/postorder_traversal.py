class Node(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

        # Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

        # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Preorder traversal
    # Root -> Left ->Right
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = res + self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
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
print(root.PostorderTraversal(root))

'''
                27
        14              35
    10      19      31      22
'''
