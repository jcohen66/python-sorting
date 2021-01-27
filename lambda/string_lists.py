def has_t(x):
    return 't' in x

def at_least_chars(x, n):
    return len(x) >= 5

strings = ['alpha', 'beta', 'gamma', 'theta']

print(list(map(lambda x: has_t(x),
               strings)))

print(list(map(lambda x: at_least_chars(x, 5),
               strings)))