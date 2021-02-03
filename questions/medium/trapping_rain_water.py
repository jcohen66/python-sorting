'''
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it
is able to trap after raining.
>>> s = Solution()
>>> s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
6
'''

class Solution(object):

    def trap(self, height):
        # helper variable to measure max height to right array
        maxSeenSoFar = 0
        maxSeenRight = [0] * len(height)
        maxSeenLeft = 0
        rainwater = 0

        # Traverse from right to left
        for i in range(len(height) - 1, 0, -1):
            if height[i] > maxSeenSoFar:
                maxSeenSoFar = height[i]
                maxSeenRight[i] = maxSeenSoFar
            else:
                maxSeenRight[i] = maxSeenSoFar

        # Traverse from left to right
        for i in range(len(height)):
            rainwater = rainwater + max(min(maxSeenLeft, maxSeenRight[i]) - height[i], 0)

            if (height[i] > maxSeenLeft):
                maxSeenLeft = height[i]

        return rainwater


