
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''
        Find the spot in the tree given
        the value of the node and the
        properties of the BST.
        '''

        # Set a ptr to the current node in the tree.
        current_node = self
        while True:
            # Check left subtree and right subtree.
            if value < current_node.value:
                if current_node.left is None:
                    # No left node so add one and break
                    current_node.left = BST(value)
                    break
                else:
                    # There is a left node so walk it.
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    # No right node so add one and break.
                    current_node.right = BST(value)
                    break
                else:
                    # There is a right node so walk it.
                    current_node = current_node.right

        # Return the added node.
        return self

    def contains(self, value):
        '''
        Walk the left or right subtree depending on
        the given value until the value is found or
        the ptr is sitting on a None.
        '''

        # Set the node ptr to the current node.
        current_node = self
        # Walk until found or off the bottom of
        # the subtree.
        while current_node is not None:
            if value < current_node.value:
                # Walk the left subtree
                current_node = current_node.left
            elif value > current_node.value:
                # Walk the right subtree
                current_node = current_node.right
            else:
                # Found the value
                return True

        return False

    def remove(self, value, parent_node=None):
        '''
        Use the optional parent_node to keep track of
        the trailing parent so you can see if there
        are child nodes.
        '''

        # Set the node ptr to the current node.
        current_node = self
        # Walk the tree
        while current_node is not None:
            # find the node
            if value < current_node.value:
                # Walk the left subtree keeping track
                # of the parent node.
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                # Walk the right subtree keeping track
                # of the parent node.
                parent_node = current_node
                current_node = current_node.right
            else:
                # two child nodes present
                if current_node.left is not None and current_node.right is not None:
                    # Switch out value with the smallest value in the subtree
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                # At the top of the tree
                elif parent_node is None:
                    if current_node.left is not None:
                        # Shift up and over
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        # Shift up and over
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        # Can either delete the entire tree
                        # by returning None as the new head
                        # or do nothing.
                        # current_node.value = None
                        pass
                # Not the top of the tree
                elif parent_node.left == current_node:
                    # Shift up and over
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    # Shift up and over
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break
        return self

    def get_min_value(self):
        '''
        Walk the left subtree to get the min value.
        '''
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value.value