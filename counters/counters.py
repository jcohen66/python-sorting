from collections import defaultdict
from collections import Counter

def top_three_letters(string):
    '''
    Given a string find the the top three most
    frequent letters.
    Should return a list of tuples, where the tuple
    contains the character and count.
    :param string:
    :return:

    >>> top_three_letters("abbccc")
    [('c', 3), ('b', 2), ('a', 1)]

    >>> top_three_letters("aabbccd")
    [('a', 2), ('b', 2), ('c', 2)]
    '''

    # 1) loop through the string and store the count
    # for each letter.
    # 2) sort the dictionary by the count and find the top
    # three most frequent letters.
    # 3) return a formatted list to match the output.
    counter = defaultdict(int)
    # 1)
    for c in string:
        counter[c] += 1

    # 2)
    top_three = sorted(
        counter,
        key=lambda k: counter[k],
        reverse=True
    )[:3]

    # 3)
    result = []
    for letter in top_three:
        result.append( (letter, counter[letter]) )


    return result


def top_three_letters_counter(string):
    '''
    Given a string find the the top three most
    frequent letters.
    Should return a list of tuples, where the tuple
    contains the character and count.
    :param string:
    :return:

    >>> top_three_letters("abbccc")
    [('c', 3), ('b', 2), ('a', 1)]

    >>> top_three_letters("aabbccd")
    [('a', 2), ('b', 2), ('c', 2)]
    '''

    return Counter(string).most_common(3)