class Solution(object):
    def merge(self, num1, m, num2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        >>> s = Solution()
        >>> num1 = [1, 2, 3, 0, 0, 0]
        >>> num2 = [4, 5, 6]
        >>> s.merge(num1, 3, num2, 3)
        [1, 2, 3, 4, 5, 6]
        >>> s = Solution()
        >>> num1 = [2, 2, 3, 0, 0, 0]
        >>> num2 = [1, 5, 6]
        >>> s.merge(num1, 3, num2, 3)
        [1, 2, 2, 3, 5, 6]
        >>> s = Solution()
        >>> num1 = [-2, 2, 3, 0, 0, 0]
        >>> num2 = [1, 5, 6]
        >>> s.merge(num1, 3, num2, 3)
        [-2, 1, 2, 3, 5, 6]
        """

        # NOTE: m is the count of FILLED elements in num1 NOT TOTAL elements in num1.

        # Get the last index of num1 given m is count of filled elements
        last = m + n - 1

        # Traverse num1 in reverse order
        while m > 0 and n > 0:
            if num1[m - 1] > num2[n - 1]:
                num1[last] = num1[m - 1]
                m -= 1
            else:
                num1[last] = num2[n - 1]
                n -= 1

            last -= 1

        # fill num1 with leftover nums2 elements
        while n > 0:
            num1[last] = num2[n - 1]
            n -= 1
            last -= 1

        return num1

# Driver

s = Solution()
num1 = [1, 2, 3, 0, 0, 0]
filled_in = [1 for i in num1 if i > 0]
filled = len(filled_in)
print(filled)
num2 = [4, 5, 6]
n = len(num2)
result = s.merge(num1, 3, num2, 3)

print(result)