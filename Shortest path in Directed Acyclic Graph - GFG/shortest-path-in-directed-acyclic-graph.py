#User function Template for python3

from typing import List
from collections import deque

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        shortest_dist = [float('inf')]*n
        shortest_dist[0] = 0
        adj = [[] for _ in range(n)]
        visited = [False]*n
        path_visited = [False]*n
        
        for u, v, w in edges:
            adj[u].append((v, w))
            
        def dfs(node, dist):
            visited[node] = True
            path_visited[node] = True
            # if dist < shortest_dist[]
            
            for adj_node, adj_weight in adj[node]:
                if not path_visited[adj_node]:
                    if dist+adj_weight<=shortest_dist[adj_node]:
                        shortest_dist[adj_node] = dist+adj_weight
                        dfs(adj_node, dist+adj_weight)
                    # dist+adj_weight < shortest_dist[adj_node]:
                    # shortest_dist[adj_node] = dist+adj_weight
                    
            path_visited[node] = False
        
        # for i in range(n):
        #     if not visited[i]:
        dfs(0, 0)
        for i in range(n):
            if shortest_dist[i] == float('inf'):
                shortest_dist[i] = -1
                
        return shortest_dist
        
        # queue = deque([(0,0)])
        # while queue:
        #     node, dist = queue.popleft()
            
        #     for adj_node, adj_weight in adj[node]:
                


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends