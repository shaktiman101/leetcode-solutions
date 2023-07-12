import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        # src = (0,0)
        # dst = (rows-1, cols-1)
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def is_valid(x, y):
            if x>=0 and x<rows and y>=0 and y<cols:
                return True
            return False
        
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (float('-inf'), 0, 0))
        
        min_effort = [[float('inf')]*cols for _ in range(rows)]
        min_effort[0][0] = 0
        
        while heap:
            path_effort, x, y = heapq.heappop(heap)
            
            for delx, dely in dirs:
                if is_valid(x+delx, y+dely):
                    to_x, to_y = x+delx, y+dely
                    effort_diff = abs(heights[to_x][to_y] - heights[x][y])
                    
                    if max(path_effort, effort_diff) < min_effort[to_x][to_y]:
                        min_effort[to_x][to_y] = max(path_effort, effort_diff)
                        heapq.heappush(heap, (max(path_effort, effort_diff), to_x, to_y))
        
        return min_effort[rows-1][cols-1]