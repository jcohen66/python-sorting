class Solution(object):
    '''
    >>> s = Solution()
    >>> l = [1,2,3,4]
    >>> s.binary_search(l, 2)
    1
    >>> l = [1,2,3,4,5,6,7,8,20,60,90]
    >>> s.binary_search(l, 2)
    1
    >>> l = [1,2,3,4,5,6,7,8,20,60,90]
    >>> s.binary_search(l, 60)
    9
    '''
    def binary_search(self, array, target):
        return self.search(array, target, 0, len(array)-1)
    
    def search(self, array, target, left, right):
        # base case
        if left > right:
            return -1
    
        middle = (left + right) // 2
        potential_match = array[middle]
    
        if target == potential_match:
            # done - return index
            return middle
        elif target < potential_match:
            return self.search(array, target, left, middle-1)
        else:
            return self.search(array, target, middle + 1, right)

