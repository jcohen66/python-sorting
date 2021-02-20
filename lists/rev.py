class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_recursive(head):
    # If head is empty or has reached the end
    # of the list.  BASE CASE
    if head is None or head.next is None:
        return head

    # Reverse the rest of the list after the head.
    tail = reverse_recursive(head.next)

    # Put first element at the end
    head.next.next = head
    head.next = None

    # Fix the head pointer
    return tail

def reverse(root):
    if not root or not root.next:
        return

    prev = None
    while root:
        next = root.next
        root.next = prev
        prev = root
        root = next

    return prev
    '''
    1 -> 2 -> 3 -> 4 -> None
    h
            p 
                    c
                        n  
        
    1) next = curr.next
    2) curr.next = prev
    3) prev = curr
    4) curr = next
    
    5) if next == None: head = prev
    '''


root = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head = reverse(root)
while head:
    print(head.value, end=" ")
    head = head.next

root = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head = reverse_recursive(root)
while head:
    print(head.value, end=" ")
    head = head.next
