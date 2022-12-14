class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         A = matrix
#         for i in range(1,len(A)):
#             for j in range(len(A[0])):

#                 #edge cases are first column and last column which only have two paths from above
#                 if j == 0:
#                     A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j + 1]) )

#                 elif (j == len(A[0]) - 1):
#                     A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j - 1]) )

#                 #every other column will have three paths coming from above
#                 else:
#                     A[i][j] = min(A[i][j] + A[i - 1][j],A[i][j] + A[i - 1][j + 1], A[i][j] + A[i - 1][j - 1])

#         # Now that minimum falling sums for each value at the bottom row have been computer
#         # We can just take the min of the bottow row to get the smallest overall path sum 
#         return min(A[len(A) - 1])

        # bottom-up: tabulation
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
            
        for i in range(1,n):
            for j in range(n):
                n1 = dp[i-1][j]
                n2 = float('inf')
                if j >= 1:
                    n2 = dp[i-1][j-1]
                n3 = float('inf')
                if j < n-1:
                    n3 = dp[i-1][j+1]
                dp[i][j] = matrix[i][j] + min(n1, n2, n3)
        return min(dp[-1])
        
        # top-down: memoization solution
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]
        def solve(row, col):
            if col < 0 or col >= n:
                return float('inf')
            if row == 0:
                return matrix[row][col]
            if dp[row][col]:
                return dp[row][col]
            n1 = solve(row-1, col)
            n2 = solve(row-1, col-1)
            n3 = solve(row-1, col+1)
            dp[row][col] = matrix[row][col]+ min(n1, n2, n3)
            return dp[row][col]
            
        min_ = float('inf')
        for j in range(n):
            min_ = min(min_, solve(n-1, j))
        return min_
    
    
        # recursive solution
        n = len(matrix)
        def solve(row, col):
            if col < 0 or col >= n:
                return 101
            if row == n-1:
                return matrix[row][col]
            n1 = solve(row+1, col)
            n2 = solve(row+1, col-1)
            n3 = solve(row+1, col+1)
            return matrix[row][col] + min(n1, n2, n3)
            
        min_ = float('inf')
        for j in range(n):
            min_ = min(min_, solve(0, j))
        return min_