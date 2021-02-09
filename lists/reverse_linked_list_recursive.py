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

class LinkedList(object):
    '''
    Reverse linked list using recursive method.
    '''
    def __init__(self):
        self.head = None

    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr + str(temp.data) + " ")
            temp = temp.next
        return linkedListStr

    def push(self, data):
        '''
        Push a new node onto the front of the list.
        '''
        temp = Node(data)
        temp.next = self.head
        self.head = temp


    def reverse(self, head):

        # If head is empty or has reached the end
        # of the list.  BASE CASE
        if head is None or head.next is None:
            return head

        # Reverse the rest of the list after the head.
        rest = self.reverse(head.next)

        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the head pointer
        return rest

# Driver
linkedList = LinkedList()
linkedList.push(20)
linkedList.push(4)
linkedList.push(15)
linkedList.push(85)

print("Given linked list")
print(linkedList)

linkedList.head = linkedList.reverse(linkedList.head)

print("Reversed linked list")
print(linkedList)

linkedList.head = linkedList.reverse(linkedList.head)

print("Back to original linked list")
print(linkedList)
