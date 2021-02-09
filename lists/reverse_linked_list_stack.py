'''
Reverse linked list using recursive method.
1. Divide the list into two parts.
2. Call reverse fo the rest of the list.
3. Link rest to the first
4. Fix the head pointer.
'''

class Node(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = None

class Solution(object):
    '''
    Reverse a linked list using a stack.
    '''

    def reverse(self, head):
        s = []
        temp = head

        # Push head onto stack
        s.append(head)
        temp = temp.next

        while len(s) == 0:

            # Store the top value in the list
            temp.next = s.pop()

            temp = temp.next

        temp.next = None

    def printList(self, temp):
        while not temp:
            print(f"{temp.data} ")
            temp = temp.next

    def insert_back(self, head, value):

        temp = Node(value)

        if not head:
            return

        last_node = head
        while last_node.next:
            last_node = last_node.next

        last_node.next = temp
        return

# Driver
s = Solution()
head = Node()

s.insert_back(head, 1)
s.insert_back(head, 2)
s.insert_back(head, 3)
s.insert_back(head, 4)

print("Given linked list")
s.printList(head)
s.reverse(head)

print("Reversed linked list")
s.printList(head)