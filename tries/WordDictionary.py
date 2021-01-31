from collections import defaultdict

def _trie():
    return defaultdict(_trie)

# TERMINAL = None
TERMINAL = '*'

class WordDictionary(object):
    def __init__(self):
        self.trie = _trie()

    def addWord(self, word):
        trie = self.trie
        for letter in word:
            trie = trie[letter]
        trie[TERMINAL]

    def search(self, word, trie=None):
        if trie is None:
            trie = self.trie

        for i, letter in enumerate(word):
            if letter == '.':
                return any(self.search(word[i+1:], t) for t in trie.itervalue())
            if letter in trie:
                trie = trie[letter]
            else:
                return False

        return TERMINAL in trie

# Driver
if __name__ == '__main__':
    t = WordDictionary()
    words = ["doe", "mode", "done"]
    for word in words:
        t.addWord(word)

    print(t.search("doe"))
    print(t.search("do"))
    print(t.search("done"))

