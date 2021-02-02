
class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.terminating = False

class Trie():

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        """
        Factory method to create a new TrieNode object
        """
        return TrieNode()

    def get_index(self, ch):
        """
        Given that we are bounded by chars a-z
        return the offset from 'a' as index.
        >>> t = Trie()
        >>> t.get_index('b')
        1
        """
        return ord(ch) - ord('a')

    def insert(self, word):
        """
        Add the undiscovered chars of the given word
        to the dictionary of the root.
        >>> t = Trie()
        >>> t.insert("add")
        >>> t.search("add")
        True
        """
        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])

            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)

        root.terminating = True

    def search(self, word):
        """
        Find a given word in the Trie.
        >>> t = Trie()
        >>> t.insert("add")
        >>> t.search("add")
        True
        """
        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])
            if not root:
                return False
            root = root.children.get(index)

        return True if root and root.terminating else False

    def delete(self, word):
        """
        Remove a given word in the Trie.
        >>> t = Trie()
        >>> t.insert("add")
        >>> t.delete("add")
        0
        >>> t.search("add")
        False
        """
        root = self.root
        lenl = len(word)

        for i in range(lenl):
            index = self.get_index(word[i])

            if not root:
                print("Word not found")
                return -1
            root = root.children.get(index)

        if not root:
            print("Word not found")
            return -1
        else:
            root.terminating = False
            return 0

    def update(self, old_word, new_word):
        """
        Replace a given old word in the Trie
        with the given new word.
        >>> t = Trie()
        >>> t.insert("add")
        >>> t.update("add", "subtract")
        >>> t.search("add")
        False
        >>> t.search("subtract")
        True
        """
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)
