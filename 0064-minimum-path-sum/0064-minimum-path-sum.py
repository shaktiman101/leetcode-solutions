class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # recursive
        # TC: 
#         def min_sum(row, col):
#             if row >= m or col >= n:
#                 return float('inf')
#             if row == m-1 and col == n-1:
#                 return grid[m-1][n-1]
            
#             sum1 = min_sum(row, col+1)
#             sum2 = min_sum(row+1, col)
#             return grid[row][col] + min(sum1, sum2)
        
#         return min_sum(0, 0)

        # memoized 
#         dp = [[-1]*n for _ in range(m)]
#         def min_sum(row, col):
#             if row >= m or col >= n:
#                 return float('inf')
#             if row == m-1 and col == n-1:
#                 return grid[m-1][n-1]
#             if dp[row][col] != -1:
#                 return dp[row][col]
            
#             sum1 = min_sum(row, col+1)
#             sum2 = min_sum(row+1, col)
#             dp[row][col] = grid[row][col] + min(sum1, sum2)
#             return dp[row][col]
        
#         return min_sum(0, 0)
    
        # bottom-up
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if i==0:
                    dp[0][j] = dp[0][j-1] + grid[i][j]
                    continue
                if j==0:
                    dp[i][0] = dp[i-1][0] + grid[i][j]
                    continue
                    
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
                
        return dp[m-1][n-1]