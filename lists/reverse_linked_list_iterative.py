class LinkedNode(object):
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    '''
    1. Initialize three pointers: prev as None, curr as head, next as None
    2. Iterate thru list starting with head
        3. Store next node: next = curr->next
        4. Change next of curr
        5. This is where the actual reversing happens: curr->next = prev
        6. Move prev and curr on step forward: prev = curr; curr = next
    7. Move head to prev
    '''
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def push(self, new_data):
        '''
        Insert a new node onto beginning of the list.
        :param new_data:
        :return:
        '''
        new_node = LinkedNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

# Driver
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked List")
llist.printList()
llist.reverse()
print("Reversed Linked List")
llist.printList()
