class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # recursive approach
        # TC: O(2^(m*n))
        # SC: O(m+n) heap stack space
#         def func(row, col):
#             if row >= m or col >= n:
#                 return 0
#             if row==m-1 and col==n-1:
#                 return 1
            
#             col_incr = func(row, col+1)
#             row_incr = func(row+1, col)
#             return col_incr+row_incr
        
#         return func(0, 0)
    
    
        # memoized approach
        # TC: O(m*n)
        # SC: O(2*m*n)
# #         dp = [[-1]*n for _ in range(m)]
# #         def func(row, col):
# #             if row >= m or col >= n:
# #                 return 0
# #             if row==m-1 and col==n-1:
# #                 return 1
# #             if dp[row][col] != -1:
# #                 return dp[row][col]
            
# #             col_incr = func(row, col+1)
# #             row_incr = func(row+1, col)
# #             dp[row][col] = col_incr+row_incr
# #             return dp[row][col]
        
#         return func(0, 0)

        # bottom-up approach
        # TC: O(m*n)
        # SC: O(m*n)
#         dp = [[1]*n for _ in range(m)]
#         for i in range(1,m):
#             for j in range(1,n):
#                 dp[i][j] = dp[i][j-1]+dp[i-1][j]
        
#         return dp[-1][-1]

        
        # space optimized bottom-up approach
        # TC: O(m*n)
        # SC: O(2*n)
        prev_row = [1]*n
        curr_row = [0]*n
        curr_row[0] = 1
        for i in range(1,m):
            for j in range(1,n):
                curr_row[j] = curr_row[j-1] + prev_row[j]  #dp[i][j-1]+dp[i-1][j]
            prev_row = curr_row
        
        return prev_row[-1]