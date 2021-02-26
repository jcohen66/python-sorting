def caesarCipherEncryptor(string, key):
    result = ''
    for c in string:
        result += encrypt(key, c)

    return result


def encrypt(key, c):
    key = key % 26
    nlc = ord(c) + key
    # if the offset value does not wrap
    # then just return the chr
    if nlc <= ord('z'):
        return chr(nlc)
    else:
        # if it does wrap, then mod it against 122 and
        # add to char just before 'a'.
        return chr((ord('a') - 1) + nlc % ord('z'))