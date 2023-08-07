class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
#         def func(left_robo, right_robo, grid):
#             if left_robo[1]<0 or left_robo[1]>=n or right_robo[1]<0 or right_robo[1]>=n:
#                 return 0
#             if left_robo[0] == m-1:
#                 return grid[left_robo[0]][left_robo[1]]
#             if right_robo[0] == m-1:
#                 return grid[right_robo[0]][right_robo[1]]
            
#             row, left_col = left_robo
#             row, right_col = right_robo
#             cherry1 = grid[row][left_col]
#             cherry2 = grid[row][right_col]
            
#             grid[row][left_col] = 0
#             c1 = cherry1 + func((row+1, left_col-1), right_robo, grid)
#             c2 = cherry1 + func((row+1, left_col), right_robo, grid)
#             c3 = cherry1 + func((row+1, left_col+1), right_robo, grid)
#             left_robo_cherry = max(c1, c2, c3)
            
            
            
#             grid[row][right_col] = 0
#             c4 = cherry2 + func(left_robo, (row+1, right_col-1), grid)
#             c5 = cherry2 + func(left_robo, (row+1, right_col), grid)
#             c6 = cherry2 + func(left_robo, (row+1, right_col+1), grid)
#             right_robo_cherry = max(c4, c5, c6)
            
#             return left_robo_cherry + right_robo_cherry
        
#         return func((0, 0), (0, n-1), grid) #+ func(0, n-1)

        # recursive approach
        # TC: O(9^(m*n))
        # SC: O(N)
#         def func(row, col1, col2, grid):
#             if col1<0 or col1>=n or col2<0 or col2>=n:
#                 return 0
#             if row == m-1:
#                 res = grid[row][col1]
#                 if col1 != col2:
#                     res += grid[row][col2]
#                 return res
            
            
#             c1 = func(row+1, col1-1, col2-1, grid)
#             c2 = func(row+1, col1-1, col2, grid)
#             c3 = func(row+1, col1-1, col2+1, grid)
            
#             c4 = func(row+1, col1, col2-1, grid)
#             c5 = func(row+1, col1, col2, grid)
#             c6 = func(row+1, col1, col2+1, grid)
            
#             c7 = func(row+1, col1+1, col2-1, grid)
#             c8 = func(row+1, col1+1, col2, grid)
#             c9 = func(row+1, col1+1, col2+1, grid)
            
#             res = grid[row][col1]
#             if col1 != col2:
#                 res += grid[row][col2]
#             return  res + max(c1, c2, c3, c4, c5, c6, c7, c8, c9)
        
#         return func(0, 0, n-1, grid)
    
    
        # memoized approach
        # TC: 
        # SC: 
        dp = [[[-1]*n for _ in range(n)] for _ in range(m)]
        def func(row, col1, col2, grid):
            if col1<0 or col1>=n or col2<0 or col2>=n:
                return 0
            if row == m-1:
                res = grid[row][col1]
                if col1 != col2:
                    res += grid[row][col2]
                return res
            if dp[row][col1][col2] != -1:
                return dp[row][col1][col2]
            
            c1 = func(row+1, col1-1, col2-1, grid)
            c2 = func(row+1, col1-1, col2, grid)
            c3 = func(row+1, col1-1, col2+1, grid)
            
            c4 = func(row+1, col1, col2-1, grid)
            c5 = func(row+1, col1, col2, grid)
            c6 = func(row+1, col1, col2+1, grid)
            
            c7 = func(row+1, col1+1, col2-1, grid)
            c8 = func(row+1, col1+1, col2, grid)
            c9 = func(row+1, col1+1, col2+1, grid)
            
            res = grid[row][col1]
            if col1 != col2:
                res += grid[row][col2]
            dp[row][col1][col2] = res + max(c1, c2, c3, c4, c5, c6, c7, c8, c9)
            
            return dp[row][col1][col2]
        
        return func(0, 0, n-1, grid)
    
    
        