#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        dirs = [(0,1),(1,0),(0,-1),(-1,0), (1,1),(-1,-1),(1,-1),(-1,1)]
        
        n, m = len(grid), len(grid[0])
        islands = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    islands += 1
                    stack = [(row, col)]
                    
                    while stack:
                        x, y = stack.pop()
                        grid[x][y] = 0
                        
                        for delx, dely in dirs:
                            tmpx, tmpy = x+delx, y+dely
                            if tmpx>=0 and tmpx<n and tmpy>=0 and tmpy<m and \
                            grid[tmpx][tmpy]==1:
                                stack.append((tmpx, tmpy))
        return islands


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends