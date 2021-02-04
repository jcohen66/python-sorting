import string



def get_key_to_letters():
    '''
    Create a map
    '''
    possible_letters = string.ascii_lowercase
    possible_keys = string.digits
    key_to_letters = {}
    start_index = 0
    for key in possible_keys:
        if key == '0':
            key_to_letters[key] = " "
        elif key == '1':
            key_to_letters[key] = ""
        else:
            num_letters = 3
            if key in {"7", "9"}:
                num_letters = 4

            letters = possible_letters[start_index: start_index + num_letters]
            key_to_letters[key] = letters
            start_index += num_letters
    return key_to_letters

# Build the map from keys to letters
KEY_TO_LETTERS = get_key_to_letters()


def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad.
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    | *        | 0 ( )   | #        |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    >>> keypad_string("157")
    'jp'
    >>> keypad_string("*")
    Traceback (most recent call last):
    ...
    AssertionError: Invalid Key
    '''


    result = ""
    count = 0
    prev_key = ""
    curr_key = ""
    valid_keys = set(string.digits)

    # Loop through the keys and add the
    for curr_key in keys:

        assert curr_key in valid_keys, "Invalid Key"

        if curr_key == "1":
            pass
        else:
            if not prev_key:
                # first key press
                prev_key = curr_key
                count = 1
            else:
                # get the map
                curr_key_letters = KEY_TO_LETTERS[curr_key]

                # press same key
                if prev_key == curr_key:
                    # press X times already
                    if count == len(curr_key_letters):
                        # get last key
                        result += curr_key_letters[-1]
                        count = 1
                    # hasn't pressed X times
                    else:
                        count += 1

                # press different key
                else:
                    prev_letters = KEY_TO_LETTERS[prev_key]
                    result += prev_letters[count - 1]
                    prev_key = curr_key
                    count = 1

    # Handle special case where key was pressed
    # multiple times but the key wouldnt have changed
    # so capture the last keypress.
    if curr_key:
        curr_key_letters = KEY_TO_LETTERS[curr_key]
        # check if there is a mapping for the
        # last key pressed.
        if len(curr_key_letters) > 0:
            result += curr_key_letters[count - 1]

    return result


