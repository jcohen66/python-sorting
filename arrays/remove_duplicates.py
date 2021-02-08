class Solution(object):
    def remove_duplicates(self, nums):
        '''
        >>> s = Solution()
        >>> arr = [0,0,1,1,1,2,2,3,3,4]
        >>> s.remove_duplicates(arr)
        5
        '''

        # Check for edge cases
        if not nums:
            return 0

        # Use the two pointer technique to remove the duplicates inplace.
        # The first element shouldnt be touched:  it's already in its correct place.
        write_pointer = 1
        # Go through each element in the array.
        for read_pointer in range(1, len(nums)):
            # If the current element we're reading is *different* to the previous element...
            if nums[read_pointer] != nums[read_pointer - 1]:
                nums[write_pointer] = nums[read_pointer]
                # And we need to now increment write_pointer, because the next element
                # should be written one space over.
                write_pointer += 1

        # This turns out to be the correct length value.
        return write_pointer