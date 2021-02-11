class Node(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def insert(self, data):
        if self.data:
            if data < self.data:
                # left subtree
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def find_val(self, lkpval):
        if lkpval < self.data:
            # search left subtree
            if not self.left:
                return(str(lkpval) + ' Not Found')
            return self.left.find_val(lkpval)
        elif lkpval > self.data:
            if not self.right:
                return(str(lkpval) + ' Not Found')
            return self.right.find_val(lkpval)
        else:
            print(str(self.data) + ' is found')

# driver
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.find_val(7))
print(root.find_val(14))





