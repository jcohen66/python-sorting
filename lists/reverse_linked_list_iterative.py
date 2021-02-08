class LinkedNode(object):
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
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
