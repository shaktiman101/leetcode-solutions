class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        # recursive
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
        dp = [[-1]*(i+1) for i in range(n)]
        def min_path_sum(row, col):
            if row > n or col > len(triangle[row]):
                return float('inf')
            if row == n-1:
                return triangle[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
                
            sum1 = min_path_sum(row+1, col)
            sum2 = min_path_sum(row+1, col+1)
            dp[row][col] = triangle[row][col] + min(sum1, sum2)
            return dp[row][col]
                        
        return min_path_sum(0,0)