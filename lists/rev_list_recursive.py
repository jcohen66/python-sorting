class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_list(head):
    if head is None or head.next == None:
        return head

    reversed_list_head = reverse_list(head.next)

    head.next.next = head
    head.next = None
    return reversed_list_head

# Driver

list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
list = reverse_list(list)
while list:
    print(list.value, end=" ")
    list = list.next
