def is_alien_sorted(words, order):
    '''
    Define new alphabet order and then check if the
    given list of words is in that order.

    Time: O(N^2 * M)
    Space: O(1)
    '''

    # Store ascii offsets to array for O(1) lookup.
    alphabet = []
    for c in order:
        alphabet.append(ord(c) - ord('a'))

    print(alphabet)

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            # only want to compare the sbortest common chars.
            min_len = min(len(words[i]), len(words[j]))
            for k in range(min_len):
                ichar = words[i][k]
                jchar = words[j][k]
                # Chars are in lexographic order then keep checking chars.
                if alphabet[ord(ichar) - ord('a')] < alphabet[ord(jchar) - ord('a')]:
                    break
                # Chars are NOT in lexographic order then no
                elif alphabet[ord(ichar) - ord('a')] > alphabet[ord(jchar) - ord('a')]:
                    return False
                # Compared all of the chars and the ith word is longer than the jth word then no.
                elif k == min_len - 1 and len(words[i]) > len(words[j]):
                    return False
    return True


# Driver
if __name__ == '__main__':

    result = is_alien_sorted(["apple", "app"], "hlabcdefgijkmnopqrstuvwxyz")
    print(result)

    result = is_alien_sorted(["hl", "ab"], "hlabcdefgijkmnopqrstuvwxyz")
    print(result)

    result = is_alien_sorted(["ab", "hl"], "hlabcdefgijkmnopqrstuvwxyz")
    print(result)

    result = is_alien_sorted(["word", "world"], "worldabcefghijkmnpqstuvwxyz")
    print(result)

    result = is_alien_sorted(["world", "word"], "worldabcefghijkmnpqstuvwxyz")
    print(result)