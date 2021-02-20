def nodeDepths(root):
    '''
    Calculate the sum of the depths of all branches.
    '''
    if not root:
        return 0

    return calc_depth(root, depth=0)


def calc_depth(root, depth):
    '''

    :param root:    Current node
    :param depth:   Depth of the current node
    :return:        Sum of the depth levels
    '''
    # Bounce off the bottom.
    if not root:
        return 0

    l, r = 0, 0

    # If there is a left branch, tell it its depth
    # given the depth of the current node and calculate
    # the sum of the branch levels.

    # Return the sum of the running depth + the left branch sum + the right branch sum.
    return depth + calc_depth(root.left, depth + 1) + calc_depth(root.right, depth + 1)


def sum_of_depths_iterative(root):
    '''
    Use a stack to keep track of depth levels.
    Note: null nodes are pushed onto the stack also.
    :param root:
    :return:
    '''
    sum_of_depths = 0
    stack = [{"node": root, "depth": 0}]

    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            # Nothing to push onto stack because no children of None
            continue
        # This only happens if node has children.
        sum_of_depths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sum_of_depths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
