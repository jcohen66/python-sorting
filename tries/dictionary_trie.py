class Trie(object):
    head = {}

    def add(self, word):
        # set the roving ptr to the head
        cur = self.head

        # iterate over chars in word
        for ch in word:
            # is this char one of the children?
            if ch not in cur:
                # no - add a key for this char
                cur[ch] = {}
            # move the roving ptr to this char
            cur = cur[ch]

        # put star marker to indicate end of word
        cur['*'] = True

    def search(self, word):
        # set the roving ptr to the head
        cur = self.head

        # iterate over the chars in the word
        for ch in word:
            # is this char one of the children?
            if ch not in cur:
                # No - done
                return False
            # Yes - move the roving ptr to this char.
            cur = cur[ch]

        # Is there an end of word char in children?
        if '*' in cur:
            # Yes - found
            return True
        else:
            # No - Not found
            return False


# Driver
dictionary = Trie()

dictionary.add("hi")
dictionary.add("hello")
dictionary.add("hel")
dictionary.add("hey")

print(dictionary.search("hi"))
print(dictionary.search("ho"))