class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        # recursive approach
        # TC: O(N)xO(3^N) = O(Nx3^N)
        # SC: O(N)
#         def func(row, col):
#             if row >= n or col >= n or col < 0:
#                 return float('inf')
#             if row == n-1:
#                 return matrix[n-1][col]
            
#             s1 = func(row+1, col-1)
#             s2 = func(row+1, col)
#             s3 = func(row+1, col+1)
#             return matrix[row][col] + min(s1, s2, s3)
            
            
#         min_ = float('inf')
#         for i in range(n):
#             min_ = min(min_, func(0,i))
            
#         return min_

#         dp = [[-1]*n for _ in range(n)]
#         def func(row, col):
#             if row >= n or col >= n or col < 0:
#                 return float('inf')
#             if row == n-1:
#                 return matrix[n-1][col]
#             if dp[row][col] != -1:
#                 return dp[row][col]
            
#             s1 = func(row+1, col-1)
#             s2 = func(row+1, col)
#             s3 = func(row+1, col+1)
#             dp[row][col] = matrix[row][col] + min(s1, s2, s3)
#             return dp[row][col]
            
            
#         min_ = float('inf')
#         for i in range(n):
#             min_ = min(min_, func(0,i))
            
#         return min_
    
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                    continue
                
                dp[i][j] = matrix[i][j] + min(float('inf') if j==0 else dp[i-1][j-1], dp[i-1][j], \
                               float('inf') if j>=n-1 else dp[i-1][j+1])
                
        return min(dp[n-1])
    
    