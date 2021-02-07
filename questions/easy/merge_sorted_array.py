class Solution(object):
    def merge_sorted_array(self, num1, num2):
        '''
        >>> s = Solution()
        >>> num1 = [1, 2, 3, 0, 0, 0]
        >>> num2 = [2, 2, 4]
        >>> s.merge_sorted_array(num1, num2)
        [1, 2, 2, 2, 3, 4]

        >>> s = Solution()
        >>> num1 = [1, 2, 3, 0, 0, 0]
        >>> num2 = [2, 3, 4]
        >>> s.merge_sorted_array(num1, num2)
        [1, 2, 2, 3, 3, 4]
        '''

        i1 = 0
        i2 = 0

        # get the number of populated cells.
        count = 0
        for i in num1:
            if i != 0:
                count += 1

        insertions = 0

        # compare n1 n2
        while i2 < len(num2):    #O(N)
            if num1[i1] >= num2[i2]:
                # make space for insert
                for n in range(len(num1)-1, i1, -1):   # O(N)
                    num1[n] = num1[n-1]
                insertions += 1
                num1[i1] = num2[i2]
                i1 += 1
                i2 += 1
            elif num1[i1] == 0:
                num1[i1] = num2[i2]
                insertions += 1
                i1 += 1
                i2 += 1
            else:
                #num1[i1] < num2[i2]:
                i1 += 1

        return num1