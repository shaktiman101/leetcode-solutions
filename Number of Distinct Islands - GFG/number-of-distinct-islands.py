#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = [[False]*m for _ in range(n)]
        
        
        def dfs(x, y, path, base):
            visited[x][y] = True
            
            for delx, dely in dirs:
                tmpx, tmpy = x+delx, y+dely
                if tmpx>=0 and tmpx<n and tmpy>=0 and tmpy<m and not visited[tmpx][tmpy]\
                and grid[tmpx][tmpy]:
                    path.append((tmpx-base[0], tmpy-base[1]))
                    dfs(tmpx, tmpy, path, base)
                    
            
        distinct_islands = set() 
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]:
                    base = (i,j)
                    path = []
                    dfs(i, j, path, base)
                    distinct_islands.add(tuple(path))
        
        return len(distinct_islands)
                    


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
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends