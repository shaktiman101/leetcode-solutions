from collections import deque
class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		n, m = len(grid), len(grid[0])
		res = [[float('inf')]*m for _ in range(n)]
		visited = [[False]*m for _ in range(n)]
		queue = deque([])
		dirs = [(0,1),(1,0),(0,-1),(-1,0)] #, (1,1),(-1,-1),(1,-1),(-1,1)]
		
		for i in range(n):
		    for j in range(m):
		        if grid[i][j] == 1:
		            res[i][j] = 0
		            queue.append((i,j,0))
		            visited[i][j] = True
# 		print(queue)
		while queue:
		    x, y, dist = queue.popleft()
		    if dist < res[x][y]:
		        res[x][y] = dist
		      #  grid[x][y]=1
		    
		  #  visited[x][y] = True
		    
		    for delx, dely in dirs:
                tmpx, tmpy = x+delx, y+dely
                if tmpx>=0 and tmpx<n and tmpy>=0 and tmpy<m and \
                grid[tmpx][tmpy]==0 and not visited[tmpx][tmpy]:
                    visited[tmpx][tmpy] = True
		            queue.append((tmpx, tmpy, dist+abs(x-tmpx)+abs(y-tmpy)))
		return res


#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends