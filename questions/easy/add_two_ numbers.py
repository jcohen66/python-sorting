class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def add_two_numbers(self, l1, l2):

        result = ListNode(0)                                    # initialize result list with placeholder node
        result_tail = result                                    # set a ptr to the dummy head
        carry = 0                                               # initialize the carry

        while l1 or l2 or carry:                                # traverse to end of lists or if there is carry
            val1 = (l1.val if l1 else 0)                        # if there is a corresponding node, take the val
            val2 = (l2.val if l2 else 0)                        # if there is a corresponding node, take the val
            carry, out = divmod(val1 + val2 + carry, 10)        # derive carry and digit

            result_tail.next = ListNode(out)                    # Set the result to the dummy_head
            result_tail = result_tail.next                      # Advance the ptr of the dummy head

            l1 = (l1.next if l1 else None)                      # advance the ptr of l1
            l2 = (l2.next if l2 else None)                      # advance the ptr of l2

        return result.next                                      # ignore the placeholder node

# Driver
s = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = s.add_two_numbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.nextd