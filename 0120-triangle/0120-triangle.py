class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # bottom-up solution
        n = len(triangle)
        dp = [[0]*(i+1) for i in range(n)]
        dp[0][0] = triangle[0][0]
        
        for i in range(1, n):
            for j in range(len(triangle[i])):
                c1 = float('inf')
                if j > 0:
                    c1 = dp[i-1][j-1]
                c2 = float('inf')
                if j < len(triangle[i])-1:
                    c2 = dp[i-1][j]
                dp[i][j] = triangle[i][j] + min(c1, c2)
        # print(dp)
        return min(dp[-1])
    
        # top-down solution
        n = len(triangle)
        dp = [[0]*(i+1) for i in range(n)]
        
        def solve(row, idx):
            if row >= n:
                return 0
            if idx > len(triangle[row])-1:
                return 0
            if row == n-1:
                return triangle[row][idx]
            if dp[row][idx]:
                return dp[row][idx]
            
            c1 = solve(row+1, idx)
            c2 = solve(row+1, idx+1)
            
            dp[row][idx] = triangle[row][idx] + min(c1, c2)
            return dp[row][idx]
            
        return solve(0, 0)
        