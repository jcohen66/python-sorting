class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        '''
        Recursive method to set a node.
        '''
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


    def postorder_traversal(self, root):
        '''
        Postorder traversal
        Left ->Right -> Root
        :param root:
        :return:
        '''
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.data)
        return res

    def preorder_traversal(self, root):
        '''
        Root -> Left -> Right
        :param root:
        :return:
        '''
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    def inorder_traversal(self, root):
        '''
        Root -> Left -> Right
        :param root:
        :return:
        '''
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res

# Driver
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.postorder_traversal(root))
print(root.preorder_traversal(root))
print(root.inorder_traversal(root))

'''
          27
    14          35
10      19   31     42
'''


