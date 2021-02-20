import unittest

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):

        return self.search(self, array)

    def search(self, node, array):
        # Handle base case bounce off bottom.
        if not node:
            return array

        # Handle edge case of root node.
        if self == node:
            array.append(node.name)

        # Traverse children depth first.
        for child in node.children:
            array.append(child.name)
            self.search(child, array)

        return array


# Driver
graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")

graph.depthFirstSearch([])
# ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])
