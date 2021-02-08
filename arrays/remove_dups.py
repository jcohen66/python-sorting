class Solution(object):
    def removeDuplicates(self, nums):
        """
        Time: O(n)
        Space: O(1)
        >>> s = Solution()
        >>> s.removeDuplicates([1,1,2])
        2
        >>> s = Solution()
        >>> s.removeDuplicates([1,2,3,3,4])
        4
        >>> s = Solution()
        >>> s.removeDuplicates([1])
        1
        >>> s = Solution()
        >>> s.removeDuplicates([])
        0
        >>> s = Solution()
        >>> s.removeDuplicates([1,1,2,2,2,2,2,2,5,5,5,5,7])
        4
        """
        # Corner case no elements
        if len(nums) == 0:
            return 0

        slow = 0
        # advance fast ptr
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                # advance slow ptr
                slow += 1
                # copy fast over slow
                nums[slow] = nums[fast]
            else:
                pass
                # just advance the fast ptr
        return slow + 1