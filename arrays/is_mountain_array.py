class Solution(object):
    def valid_mountain_array(self, A):
        '''
        Calculate whether the elements ascend to a peak
        and then descend at a rate that all element conform
        to the slope at N-1 elements.

        >>> s = Solution()
        >>> s.valid_mountain_array([1,0,1])
        False
        >>> s = Solution()
        >>> s.valid_mountain_array([1,4,1])
        True
        '''
        N = len(A)
        i = 0

        # going up
        while i + 1 < N and A[i] < A[i+1]:
            i += 1

        # peak cant be first or last
        if i == 0 or i == N-1:
            return False

        # Going down
        while i + 1 < N and A[i] > A[i+1]:
            i += 1

        # All of the elements conform
        return i == N-1