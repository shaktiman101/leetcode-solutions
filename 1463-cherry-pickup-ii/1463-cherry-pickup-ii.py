class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # bottom-up: tabulation
        m, n = len(grid), len(grid[0])
        dp = [[[0]*n for _ in range(n)] for _ in range(m)]
                    
        for i in range(m-1, -1, -1):
            for j in range(n):
                for k in range(n):
                    if i == m-1:
                        dp[i][j][k] = grid[i][j]
                        if j != k:
                            dp[i][j][k] += grid[i][k]
                    else: 
                        c2,c3,c4,c5,c6,c7,c8,c9=[float('-inf')]*8
                        c1 = dp[i+1][j][k]
                        if k > 0:
                            c2 = dp[i+1][j][k-1]
                        if k < n-1:
                            c3 = dp[i+1][j][k+1]

                        if j > 0:
                            c4 = dp[i+1][j-1][k]
                            if k > 0:
                                c5 = dp[i+1][j-1][k-1]
                            if k < n-1:
                                c6 = dp[i+1][j-1][k+1]

                        if j < n-1:
                            c7 = dp[i+1][j+1][k]
                            if k > 0:
                                c8 = dp[i+1][j+1][k-1]
                            if k < n-1:
                                c9 = dp[i+1][j+1][k+1]
                        dp[i][j][k] = grid[i][j] + max(c1,c2,c3,c4,c5,c6,c7,c8,c9)
                        if j != k:
                            dp[i][j][k] += grid[i][k]        
        return dp[0][0][n-1]
        # print(dp)
        
        # top-down memoization
        m, n = len(grid), len(grid[0])
        dp = [[[0]*n for _ in range(n)] for _ in range(m)]
        
        def func(row, col1, col2):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return float('-inf')
            if row == m-1:
                if col1 == col2:
                    return grid[row][col1]
                return grid[row][col1]+grid[row][col2]
            if dp[row][col1][col2]:
                return dp[row][col1][col2]
            c1 = func(row+1, col1, col2)
            c2 = func(row+1, col1, col2-1)
            c3 = func(row+1, col1, col2+1)
            
            c4 = func(row+1, col1-1, col2)
            c5 = func(row+1, col1-1, col2-1)
            c6 = func(row+1, col1-1, col2+1)
            
            c7 = func(row+1, col1+1, col2)
            c8 = func(row+1, col1+1, col2-1)
            c9 = func(row+1, col1+1, col2+1)
            
            dp[row][col1][col2] = grid[row][col1] + max(c1,c2,c3,c4,c5,c6,c7,c8,c9)
            if col1 != col2:
                dp[row][col1][col2] += grid[row][col2] 
            return dp[row][col1][col2]
        
        z= func(0, 0, n-1)
        print(dp)
        return z
    
        
        # recursive solution
        m, n = len(grid), len(grid[0])
        def func(row, col1, col2):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n or col1==col2:
                return float('-inf')
            if row == m-1:
                return grid[row][col1]+grid[row][col2]
            
            c1 = func(row+1, col1, col2)
            c2 = func(row+1, col1, col2-1)
            c3 = func(row+1, col1, col2+1)
            
            c4 = func(row+1, col1-1, col2)
            c5 = func(row+1, col1-1, col2-1)
            c6 = func(row+1, col1-1, col2+1)
            
            c7 = func(row+1, col1+1, col2)
            c8 = func(row+1, col1+1, col2-1)
            c9 = func(row+1, col1+1, col2+1)
            
            return grid[row][col1] + grid[row][col2] + max(c1,c2,c3,c4,c5,c6,c7,c8,c9)
        
        return func(0, 0, n-1)
            
        
        