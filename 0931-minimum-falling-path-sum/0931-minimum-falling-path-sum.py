class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
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