from collections import deque
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		dirs = [(0,1),(1,0),(0,-1),(-1,0)]
		
		n, m = len(grid), len(grid[0])
# 		total_time = [[float('inf')]*m for _ in range(n)]
        # visited = [[False]*m for _ in range(n)]
		queue = deque([])
		
		for row in range(n):
		    for col in range(m):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))     # index_X, index_Y, time
            
        # global_time = float('inf')
        time = 0
        while queue:
            x, y, time = queue.popleft()
            # grid[x][y] = 3
            # visited
            
            for delx, dely in dirs:
                tmpx, tmpy = x+delx, y+dely
                if tmpx>=0 and tmpx<n and tmpy>=0 and tmpy<m and \
                grid[tmpx][tmpy]==1:
                    grid[tmpx][tmpy] = 3
                    queue.append((tmpx, tmpy, time+1))
        #     if time:
        #         global_time = min(time, global_time)
        # if global_time == float('inf'):
        #     return 0
        for row in range(n):
		    for col in range(m):
                if grid[row][col] == 1:
                    return -1
        return time #global_time

#{ 
 # Driver Code Starts
from queue import Queue


T=int(input())
for i in range(T):
	n, m = map(int, input().split())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.orangesRotting(grid)
	print(ans)

# } Driver Code Ends