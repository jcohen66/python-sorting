class Link(object):
    def __init__(self, key=0, next=None):
        self.key = key
        self.next = next

    def __repr__(self):
        if not self.next:
            return f"Link({self.key})"
        return f"Link({self.key}, {self.next})"


'''
Suboptimal solution.
look at the front value of all the linked lists
find the minimum, put it in the result linked list
"remove" that value that we've added
keep going until there are no more values to add

k - length of linked_lists
n - max length of any linked list
k*n - upper bound of number of values in all linked lists


'''

def merge_k_linked_lists(linked_lists):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists([Link(1, Link(2)), Link(3, Link(4))]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists([    # O(k)
    ...    Link(1, Link(2)),
    ...    Link(2, Link(4)),
    ...    Link(3, Link(3))
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''
    # make a deep copy so we can mutate (bad idea)
    copy_linked_lists = linked_lists[:]                 # O(n)
    result = Link(0)
    pointer = result

    # How many times does the while look run?
    # k*n
    while any(copy_linked_lists):                       # O(k)
        front_vals = [
            link.key for link in copy_linked_lists if link
        ] #O(k)
        min_val = min(front_vals)                       # O(k)
        for i, link in enumerate(copy_linked_lists):    # O(k)
            if link and link.key == min_val:
                pointer.next = Link(link.key)
                pointer = pointer.next
                copy_linked_lists[i] = link.next

    # brute force: Final runtime: O(k*n*log(k*n))
    # final runtime: O(k*n*k)
    return result.next