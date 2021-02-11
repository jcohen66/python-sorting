class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverse(self, head):
        '''
        >>> head = ListNode(1)
        >>> head.next = ListMode(2)
        >>> s = Solution()
        >>> s.reverse(head)
        head
        :param head:
        :return:
        '''
        '''
        :param head: 
        :return: 
        '''
        prev = None

        print(head)
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        print(prev)
        return prev

# Driver
s = Solution()
head = ListNode(1)
head.next = ListNode(2)
print(s.reverse(head))