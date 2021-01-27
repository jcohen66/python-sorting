import string
from timeit import timeit


def is_upper(s):
    for letter in s:
        if letter not in string.ascii_uppercase:
            return False
    return True

uppercase_set = set(string.ascii_uppercase)
def is_upper_using_set(s):
    for letter in s:
        if letter not in uppercase_set:
            return false
    return True

def is_upper_cleaner(s):
    """
    Uses generator and short circuits
    :param s:
    :return:
    """
    return all(letter in uppercase_set for letter in s)

whitespace_set = string.whitespace
def remove_whitespace(s):
    return ''.join(letter for letter in s if letter not in whitespace_set)

print(remove_whitespace("HELLO WORLD"))

print(string.ascii_letters)
print(string.punctuation)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.hexdigits)
print(string.octdigits)
print(string.printable)

