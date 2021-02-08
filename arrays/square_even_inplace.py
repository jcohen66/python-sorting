class Solution(object):
    def square_even(self, arr):
        '''
        >>> s = Solution()
        >>> s.square_even([1,2,3])
        [1, 2, 9]

        >>> s = Solution()
        >>> s.square_even([])
        []
        '''

        if not arr or len(arr) == 0:
            return arr

        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] = arr[i] * arr[i]

        return arr