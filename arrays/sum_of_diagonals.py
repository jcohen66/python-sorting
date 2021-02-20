class Solution(object):

    def diagonal_sum(self, matrix):
        n = len(matrix)
        sum = 0
        for i in range(n):
            sum += matrix[i][i] + matrix[i][n-i-1]
        if n % 2 == 1:
            sum -= matrix[n//2][n//2]

        return sum

# Driver
s = Solution()
m = [[1,2,3], [4,5,6], [7,8,9]]
print(s.diagonal_sum(m))

m = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
print(s.diagonal_sum(m))