class Solution(object):
    def matrix_mult(self, m1, m2, mat1, n1, n2, mat2):
        '''
        Multiplies two matrices mat1[][]
        and mat2[] and prints result.
        (m1) x (m2) are dimensions of given
        matrices.
        >>> s = Solution()
        >>> mat1 = [[2, 4], [3, 4]]
        >>> mat2 = [[1, 2], [1, 3]]
        >>> s.matrix_mult(2,2, mat1, 2, 2, mat2)
        [[6, 16], [7, 18]]
        '''

        res = [[0 for x in range(m2)]
               for y in range(m1)]

        for i in range(m1):
            for j in range(n2):
                res[i][j] = 0
                for x in range(m2):
                    res[i][j] += (mat1[i][x] * mat2[x][j])

        # Output the result
        # for i in range(m1):
        #     for j in range(n2):
        #         print(res[i][j], end=" ")
        #     print()

        return res
# Driver
if __name__ == '__main__':

    mat1 = [[2, 4], [3, 4]]
    mat2 = [[1, 2], [1, 3]]
    m1, m2, n1, n2 = 2, 2, 2, 2

    s = Solution()
    s.matrix_mult(m1, m2, mat1, n1, n2, mat2)


