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
        i = 0
        number_of_elements = len(nums)
        while i < number_of_elements:
            if nums[i] == val:
                # swap with last element for fast delete
                nums[i] = nums[number_of_elements - 1]
                # reduce array size by 1
                number_of_elements -= 1
            else:
                # move the ptr
                i += 1

        return number_of_elements