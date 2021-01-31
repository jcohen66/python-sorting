class Trie(object):

    head = {}

    def add(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        """
            Given a Trie and strings 'hi' and 'hello'
            >>> dictionary = Trie()
            >>> dictionary.add('hi')
            >>> dictionary.add('hello')
            >>> dictionary.search('hi')
            True
            >>> dictionary.search('hello')
            True
            >>> dictionary.search('apple')
            False
            >>> dictionary.search('hel')
            False
            >>> dictionary.search('hey')
            False
            """
        cur = self.head

        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        else:
            return False

# Driver

tries = Trie()

tries.add("hi")
tries.add("Hello")
print(tries.head)