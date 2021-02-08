class Solution(object):
    def removeElement(self, nums, val):
        """
        Time: O(n)
        Space: O(1)

        >>> s = Solution()
        >>> s.removeElement([3,3], 3)
        0
        >>> s = Solution()
        >>> s.removeElement([3,2,2,3], 3)
        2
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow