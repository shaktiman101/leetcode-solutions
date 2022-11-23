class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # bottom-up solution
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
                
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    w1 = dp[i-1][j]
                    w2 = dp[i][j-1]
                    dp[i][j] = w1 + w2
        return dp[m-1][n-1]
    
    
        # top-down solution
        m, n = len(obstacleGrid), len(obstacleGrid[0])        
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        def solve(row, col):
            if row < 0 or col < 0:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == 0 and col == 0:
                return 1
            if dp[row][col]:
                return dp[row][col]
            w1 = solve(row-1, col)
            w2 = solve(row, col-1)
            dp[row][col] = w1+w2
            return dp[row][col]
        
        return solve(m-1, n-1)
    
        
        # recursive solution
        m, n = len(obstacleGrid), len(obstacleGrid[0])        
        def solve(row, col):
            if row < 0 or col < 0:
                return 0
            if row == 0 and col == 0:
                return 1
            w1 = 0
            if obstacleGrid[row-1][col] == 0:
                w1 = solve(row-1, col)
            w2 = 0
            if obstacleGrid[row][col-1] == 0:
                w2 = solve(row, col-1)
            return w1+w2
        
        return solve(m-1, n-1)