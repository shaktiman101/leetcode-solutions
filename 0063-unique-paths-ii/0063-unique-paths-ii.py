class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        # recursive approach
        # TC: O(2*(m*n))
        # SC: O(m*n)
#         def unique_paths(row, col):
#             if row >= m or col >= n:
#                 return 0
#             if row == m-1 or col == n-1:
#                 return 1
            
#             col_ways, row_ways = 0, 0
#             if col < n and obstacleGrid[row][col+1] == 0:
#                 col_ways = unique_paths(row, col+1)
#             if row < m and obstacleGrid[row+1][col] == 0:
#                 row_ways = unique_paths(row+1, col)
#             return col_ways+row_ways
        
#         return unique_paths(0, 0)


        # memoized approach
        dp = [[-1]*n for _ in range(m)]
        def unique_paths(row, col):
            if row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if dp[row][col] != -1:
                return dp[row][col]
            
            col_ways, row_ways = 0, 0
            if col+1 < n and obstacleGrid[row][col+1] == 0:
                col_ways = unique_paths(row, col+1)
            if row+1 < m and obstacleGrid[row+1][col] == 0:
                row_ways = unique_paths(row+1, col)
            dp[row][col] = col_ways+row_ways
            return dp[row][col]
        
        return unique_paths(0, 0)
        
        