class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"

class Solution(object):
    def merge_two_lists(self, l1, l2):
        '''
        Merge two sorted linked lists.
        >>> s = Solution()
        >>> l1 = ListNode(1, ListNode(2, ListNode(3)))
        >>> l2 = ListNode(4, ListNode(5, ListNode(6)))
        >>> s.merge_two_lists(l1, l2)
        Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
        '''

        # Placeholder for result head
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                # add l1 node to result
                tail.next = l1
                # advance to next node in l1
                l1 = l1.next
            else:
                # add l2 node to result
                tail.next = l2
                # advance to next node in l2
                l2 = l2.next

            # advance to next node in result
            tail = tail.next

        # tack on to result any remaining nodes from l1 or l2.
        # if lengths were different.
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        # make sure to return node after placeholder.
        return dummy.next
