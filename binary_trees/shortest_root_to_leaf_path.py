# Python3 program to print first
# shortest root to leaf path

# Binary tree node
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive function used by leftMostShortest
# to print the first shortest root to leaf path
def printPath(Data, parent):
    # If the root's data is same as
    # its parent data then return
    if parent[Data] == Data:
        return

    # Recur for the function printPath
    printPath(parent[Data], parent)

    # Print the parent node's data
    print(parent[Data], end=" ")


# Function to perform level order traversal
# until we find the first leaf node
def leftMostShortest(root):
    # Queue to store the nodes
    q = []

    # Push the root node
    q.append(root)

    # Initialize the value of first
    # leaf node to occur as -1
    LeafData = -1

    # To store the current node
    temp = None

    # Map to store the parent node's data
    parent = {}

    # Parent of root data is set
    # as it's own value
    parent[root.data] = root.data

    # We store first node of the
    # smallest level
    while len(q) != 0:
        temp = q.pop(0)

        # If the first leaf node has been
        # found set the flag variable as 1
        if not temp.left and not temp.right:
            LeafData = temp.data
            break

        else:

            # If current node has left
            # child, push in the queue
            if temp.left:
                q.append(temp.left)

                # Set temp's left node's parent as temp
                parent[temp.left.data] = temp.data

                # If current node has right
            # child, push in the queue
            if temp.right:
                q.append(temp.right)

                # Set temp's right node's parent
                # as temp
                parent[temp.right.data] = temp.data

                # Recursive function to print the first
    # shortest root to leaf path
    printPath(LeafData, parent)

    # Print the leaf node of the
    # first shortest path
    print(LeafData, end=" ")


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(7)
    root.left.left.left = Node(10)
    root.left.left.right = Node(11)
    root.right.right.left = Node(8)

    leftMostShortest(root)