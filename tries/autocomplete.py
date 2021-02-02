"""
Solution to autocomplete problem using Tries.
"""
class Node(object):
    """
    Implementation of Trie
    """
    def __init__(self, prefix, children=None):
        self.prefix = prefix
        self.children = {}

class Autocomplete(object):

    def __init__(self, dict, trie=None):
        self.dict = dict
        self.trie = Node("")
        for s in dict:
            self.insert_word(s)

    def insert_word(self, s):
        """
        Iterate thru each char in the string.
        If the char is not already in the trie then add it.
        """
        curr = self.trie
        for i in range(len(s)):
            if s[i] not in curr.children:
                curr.children[s[i]] = Node(s[:i+1])
            curr = curr.children[s[i]]
            if  len(s) -1:
                curr.isWord = True

    def get_words_for_prefix(self, pre):
        """
        Find all words in trie that start with prefix
        """
        results = []

        curr = self.trie
        # Walk the chars in prefix
        for c in pre:
            # Walk the chars in children
            if c in curr.children:
                curr = curr.children[c]
            else:
                return results

        # At the end of the prefix, find all child words
        self.find_all_child_words(curr, results)
        return results

    def find_all_child_words(self, node, results):
        if node.isWord:
            results.append(node.prefix)
        for c in node.children.keys():
            # Recurse and make sure to move the c
            self.find_all_child_words(node.children[c], results)
# Driver
strings = ["abc", "acd", "bcd", "def", "a", "aba"]
a = Autocomplete(strings)

print(a.get_words_for_prefix("ab"))