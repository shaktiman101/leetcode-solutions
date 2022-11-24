class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #top-down solution
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        def solve(row, col):
            if row < 0 or col < 0:
                return 0
            if row==0 and col==0:
                return grid[0][0]
            if dp[row][col]:
                return dp[row][col]
            c1, c2 = float('inf'), float('inf')
            if row > 0:
                c1 = solve(row-1, col)
            if col > 0:
                c2 = solve(row, col-1)
            dp[row][col] = grid[row][col] + min(c1, c2)
            return dp[row][col]
            
        solve(m-1, n-1)
        return dp[m-1][n-1]
    
        #recusrive solution
        m, n = len(grid), len(grid[0])
        
        def solve(row, col):
            if row < 0 or col < 0:
                return 0
            if row==0 and col==0:
                return grid[0][0]
            c1, c2 = float('inf'), float('inf')
            if row > 0:
                c1 = solve(row-1, col)
            if col > 0:
                c2 = solve(row, col-1)
            return grid[row][col] + min(c1, c2)
            
        return solve(m-1, n-1)
        