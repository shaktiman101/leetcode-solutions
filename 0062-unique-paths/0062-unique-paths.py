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
        dp = [[-1]*n for _ in range(m)]
        def func(row, col):
            if row >= m or col >= n:
                return 0
            if row==m-1 and col==n-1:
                return 1
            if dp[row][col] != -1:
                return dp[row][col]
            
            col_incr = func(row, col+1)
            row_incr = func(row+1, col)
            dp[row][col] = col_incr+row_incr
            return dp[row][col]
        
        return func(0, 0)