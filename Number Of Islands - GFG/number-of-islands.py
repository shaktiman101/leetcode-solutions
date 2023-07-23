#User function Template for python3

from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        grid = [[0]*cols for _ in range(rows)]
        parent = [-1 for i in range(rows*cols)]
        size = [0 for _ in range(rows*cols)]
        
        islands = 0
        def find_uparent(X):
            if X == parent[X]:
                return X
            parent[X] = find_uparent(parent[X])
            return parent[X]
            
        def union(u, v):
            pu = find_uparent(u)
            pv = find_uparent(v)
            
            if pu == pv:
                return
            
            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
                for node, pa in enumerate(parent):
                    if pa == pu:
                        parent[node] = find_uparent(node)
            else:
                parent[pv] = pu
                size[pu] += size[pv]
                for node, pa in enumerate(parent):
                    if pa == pv:
                        parent[node] = find_uparent(node)
                
        res = []
        for x, y in operators:
            curr_node = cols*x + y
            grid[x][y] = 1
            parent[curr_node] = curr_node
            size[curr_node] = 1
            
            for delx, dely in dirs:
                changedx, changedy = x+delx, y+dely
                
                if changedx>=0 and changedx<rows and changedy>=0 and changedy<cols and\
                grid[changedx][changedy] == 1:
                    prev_node = changedx*cols + changedy
                    union(prev_node, curr_node)
            
            islands = 0
            for i in range(rows*cols):
                if i == parent[i]:
                    islands += 1
            res.append(islands) 
                  
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends