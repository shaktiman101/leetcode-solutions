#User function Template for python3
import heapq
class Solution:
        
    def MinimumEffort(self, a):
        rows, cols = len(a), len(a[0])
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, 0, 0)) # max_effort, x, y
        
        effort_mat = [[float('inf')]*cols for _ in range(rows)]
        effort_mat[0][0] = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def is_valid(x, y):
            if x>=0 and x<rows and y>=0 and y<cols:
                return True
            return False
            
        while heap:
            max_effort, x, y = heapq.heappop(heap)
            for delx, dely in dirs:
                to_x, to_y = x+delx, y+dely
                if is_valid(to_x, to_y):
                    curr_effort = abs(a[x][y]-a[to_x][to_y])
                    if max(max_effort, curr_effort) < effort_mat[to_x][to_y]:
                        effort_mat[to_x][to_y] = max(max_effort, curr_effort)
                        heapq.heappush(heap, (max(max_effort, curr_effort), to_x, to_y))
                        
        return effort_mat[rows-1][cols-1]
                    
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n,m=map(int,input().split())
        a=[]
        for i in range(n):
            li=list(map(int,input().split()))
            a.append(li)
        ob = Solution()
        ans = ob.MinimumEffort(a)
        print(ans)
        tc -= 1
# } Driver Code Ends