class Link(object):
    def __init__(self, key=0, next=None):
        self.key = key
        self.next = next

    def __str__(self):
        if not self.next:
            return f"Link({self.key})"
        return f"Link({self.key}, {self.next})"


'''
Brute force solution.
Put all the values of all the linked
list into a list.
Sort the list and create a final list from
those valuse.
# k - length of linked lists
# n - max length of any linked list
# k*n - upper band of the number of values in all linked lists
'''

def merge_k_linked_lists(linked_lists):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists([Link(1, Link(2)), Link(3, Link(4))]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists([
    ...    Link(1, Link(2)),
    ...    Link(2, Link(4)),
    ...    Link(3, Link(3))
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''


    lst = []
    # takes O(k*n)
    for node in linked_lists:           # O(k)
        while node:                     # O(n)
            lst.append(node.key)
            node = node.next

    # O(k*n*log(k*n))
    sorted_vals = sorted(lst)

    result = Link(0)
    # preserve the head position
    pointer = result

    # create a new list from the sorted vals
    # O(k*n)
    for i in sorted_vals:
        # print(result, pointer)
        pointer.next = Link(i)
        pointer = pointer.next

    # return the preserved pointer
    # final runtime:  O(k*n*log(k*n))
    return result.next
