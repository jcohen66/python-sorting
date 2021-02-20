class TreeNode(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution(object):

    def insert_into_BST(self, root, value):
        node = root
        if not root:
            return TreeNode(value)

        while True:
            if value >= node.value:
                if node.right:
                    node = node.right
                    continue
                else:
                    node.right = TreeNode(value)
                    break
            else:
                if node.left:
                    node = node.left
                    continue
                else:
                    node.left = TreeNode(value)
                    break

        return root

# Driver
s = Solution()
root = None
root = s.insert_into_BST(root, 10)
s.insert_into_BST(root, 20)
print(root)

