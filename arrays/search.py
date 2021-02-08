class Solution(object):
    def linear_search(self, arr, length, element):
        '''
        >>> s = Solution()
        >>> s.linear_search([1,2,3], 3, 2)
        True

        '''
        if arr is None or length == 0:
            return False

        for i in range(len(arr)):
            if arr[i] == element:
                return True

        return False