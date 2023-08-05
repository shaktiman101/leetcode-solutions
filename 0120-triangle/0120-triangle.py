class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        # recursive
        # TC: O(N^2) as func iterates over each ele
        # SC: O(N) recursion heap stack space
#         def min_path_sum(row, col):
#             if row > n or col > len(triangle[row]):
#                 return float('inf')
#             if row == n-1:
#                 return triangle[row][col]
            
#             sum1 = min_path_sum(row+1, col)
#             sum2 = min_path_sum(row+1, col+1)
#             return triangle[row][col] + min(sum1, sum2)
                        
#         return min_path_sum(0,0)
    
    
        # memoized
        # TC: 
        # SC: O(N^2) for dp array, O(N) for recursion heap stack space
        dp = [[-1]*(i+1) for i in range(n)]
        def min_path_sum(row, col):
            # if row > n or col > len(triangle[row]):
            #     return float('inf')
            if row == n-1:
                return triangle[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
                
            sum1 = triangle[row][col] + min_path_sum(row+1, col)
            sum2 = triangle[row][col] + min_path_sum(row+1, col+1)
            dp[row][col] = min(sum1, sum2)
            return dp[row][col]
                        
        return min_path_sum(0,0)
    
    
        # bottom-up
        dp = [[float('inf')]*(i+2) for i in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i+1):
                sum2 = float('inf')
                if j > 0:
                    sum2 = dp[i-1][j-1]
                dp[i][j] = triangle[i][j] + min(dp[i-1][j], float('inf') if j<1 else dp[i-1][j-1])
        
        return min(dp[n-1])