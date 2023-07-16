#User function Template for python3

from typing import List

from collections import deque
class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = [[False]*m for _ in range(n)]
        queue = deque([])
            
        # def dfs(x, y):
        #     visited[x][y] = True
            
        #     for delx, dely in dirs:
        #         tmpx, tmpy = x+delx, y+dely 
        #         if tmpx>=0 and tmpx<n and tmpy>=0 and tmpy<m and \
        #         grid[tmpx][tmpy]==1 and not visited[tmpx][tmpy]:
        #             dfs(tmpx, tmpy)
            
        def bfs(queue):
            while queue:
                x, y = queue.popleft()
                
                for delx, dely in dirs:
                    tmpx, tmpy = x+delx, y+dely 
                    if tmpx>=0 and tmpx<n and tmpy>=0 and tmpy<m and \
                    grid[tmpx][tmpy]==1 and not visited[tmpx][tmpy]:
                        visited[tmpx][tmpy] = True
                        queue.append((tmpx, tmpy))
                    
            
        for row in [0,n-1]:
            for col in range(m):
                if not visited[row][col] and grid[row][col] == 1:
                    # dfs(row, col)
                    queue.append((row, col))
                    visited[row][col] = True
                    bfs(queue)
                    
        for row in range(n):
            for col in [0, m-1]:
                if not visited[row][col] and grid[row][col] == 1:
                    # dfs(row, col)
                    queue.append((row, col))
                    visited[row][col] = True
                    bfs(queue)
                    
        count = 0
        for row in range(n):
            for col in range(m):
                if not visited[row][col] and grid[row][col] == 1:
                    count += 1
                    
        # print(visited)
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends