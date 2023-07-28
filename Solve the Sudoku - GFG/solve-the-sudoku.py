#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        
        def is_safe(row_orig, col_orig, num):        
        
            col = col_orig-1
            while col >= 0:
                if grid[row_orig][col] == num:
                    return False
                col -= 1
                
            col = col_orig+1
            while col < 9:
                if grid[row_orig][col] == num:
                    return False
                col += 1
                
            row = row_orig-1
            while row >= 0:
                if grid[row][col_orig] == num:
                    return False
                row -= 1
                
            row = row_orig+1
            while row < 9:
                if grid[row][col_orig] == num:
                    return False
                row += 1
            
            row_multi = row_orig//3
            col_multi = col_orig//3
            for i in range(3*row_multi, 3*row_multi+3):
                for j in range(3*col_multi, 3*col_multi+3):
                    if grid[i][j] == num:
                        return False
                    
            return True
                
        
        def backtrack(row, col):
            if row == 9:
                return True
            
            if col >= 9:
                # row = col//9
                # col = col%9
                return backtrack(row+1, 0)
                
            if grid[row][col] != 0:
                return backtrack(row, col+1)
    
            for num in range(1,10):
                if is_safe(row, col, num):
                    grid[row][col] = num
                    if backtrack(row, col+1):
                        return True
                    grid[row][col] = 0
                
            return False
            
        return backtrack(0, 0)
        
        # def backtrack():
        #     for i in range(9):
        #         for j in range(9):
        #             if grid[i][j] != 0:
        #                 continue
                    
        #             for num in range(1,10):
        #                 if is_safe(i,j,num):
        #                     grid[i][j] = num
        #                     if backtrack():
        #                         return True
        #                     grid[i][j] = 0
        #             return False
        #     return True
        
        # return backtrack()
        
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=" ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends