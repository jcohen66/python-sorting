stack = []

# append to push element onto stack
stack.append('a')
stack.append('b')
stack.append('c')

print('initial stack')
print(stack)

# pop() to pop element from stack in LIFO order
print('\nElements popped from stack: ')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped: ')
print(stack)

try:
    stack.pop()
except IndexError(e):
    print(e)


