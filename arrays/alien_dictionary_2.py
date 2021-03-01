class Solution(object):
    def isAlienSorted(self, words, order):
        '''
        >>> s = Solution()
        >>> s.isAlienSorted(["apple", "app"], "abcdefghijklomnopqrstuvwxyz")
        False
        >>> s = Solution()
        >>> s.isAlienSorted(["app", "apple"], "abcdefghijklomnopqrstuvwxyz")
        True
        >>> s = Solution()
        >>> s.isAlienSorted(["world", "word"], "hlabcdefgijkomnopqrstuvwxyz")
        True
        '''
        # Load the letters and corresponding indexes into a dict.
        dict = {}
        # Use enumeration to get the index (x) along with the value (y)
        for x,y in enumerate(order):
            dict[y] = x

        # Scan the word list comparing adjacent words.
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            # Scan letters of smaller word
            for i in range(min(len(word1), len(word2))):
                # Do the words match?
                if word1[i] != word2[i]:
                    # Compare chars for indexes in common
                    if dict[word1[i]] > dict[word2[i]]:
                        return False
                    break

            else:
                # The shorter word wins
                if len(word1) > len(word2):
                    return False

        return True