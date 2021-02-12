class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    '''
    >>> s = Solution()
    >>> root = TreeNode(1, TreeNode(2, TreeNode(3)))
    >>> s.preorder(root)
    [1,2,3]
    '''
    def preorder(self, root):
        stack = []
        output = []
        if root is None:
            return output

        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                output.append(node)
                stack.append(node.right)
                stack.append(node.left)
        return output