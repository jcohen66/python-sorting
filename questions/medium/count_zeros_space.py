class Solution(object):
    def duplicateZeros(self, arr):
        '''
        Uses extra space to solve.
        Time: O(n)
        Space: O(n)
        >>> s = Solution()
        >>> arr = [1, 0, 1, 1, 0]
        >>> s.duplicateZeros(arr)
        [1, 0, 0, 1, 1]
        '''
        org = arr[:] # Copy values of arr to org
        i = j = 0
        n = len(arr)
        while j < n:
            arr[j] = org[i]
            j += i
            if org[i] == 0:  # Copy twice if org[i] == 0
                if j < n:
                    arr[j] = org[i]
                    j += 1
                i += 1

