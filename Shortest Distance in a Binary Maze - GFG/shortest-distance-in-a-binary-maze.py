#User function Template for python3

from typing import List
import heapq

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        direction = [(0,1),(1,0),(0, -1),(-1,0)]
        n, m = len(grid), len(grid[0])
        
        def is_valid(x, y):
            if x >=0 and x < n and y >=0 and y < m and grid[x][y] == 1:
                return True
            return False
            
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, source[0], source[1]))
        min_dist = [[float('inf')]*m for _ in range(n)]
        min_dist[source[0]][source[1]] = 0
        
        while heap:
            curr_dist, currx, curry = heapq.heappop(heap)
            for changex, changey in direction:
                changedx, changedy = currx+changex, curry+changey
                if is_valid(changedx, changedy) and curr_dist+1 < min_dist[changedx][changedy]:
                    min_dist[changedx][changedy] = curr_dist+1
                    heapq.heappush(heap, (curr_dist+1, changedx, changedy))
        
        if min_dist[destination[0]][destination[1]] == float('inf'):
            return -1
        return min_dist[destination[0]][destination[1]]
        
                    
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends