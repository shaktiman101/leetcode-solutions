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
        dp = [[-1]*n for _ in range(m)]
        def min_sum(row, col):
            if row >= m or col >= n:
                return float('inf')
            if row == m-1 and col == n-1:
                return grid[m-1][n-1]
            if dp[row][col] != -1:
                return dp[row][col]
            
            sum1 = min_sum(row, col+1)
            sum2 = min_sum(row+1, col)
            dp[row][col] = grid[row][col] + min(sum1, sum2)
            return dp[row][col]
        
        return min_sum(0, 0)