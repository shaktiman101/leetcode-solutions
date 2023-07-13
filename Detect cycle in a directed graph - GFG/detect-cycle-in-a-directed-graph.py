#User function Template for python3

from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # # using DFS approach
        # global_visited = [False]*V
        # visited = [False]*V
        # cycle = False
        
        # def dfs(node, visited):
            
        #     global_visited[node] = True
        #     visited[node] = True 
            
        #     for adj_node in adj[node]:
        #         if not global_visited[adj_node]:
        #             if dfs(adj_node, visited):
        #                 return True
        #         else:
        #             if visited[adj_node]:
        #                 return True
        #     visited[node] = False
        #     return False
                    
        
        # for i in range(V):
        #     if not global_visited[i] and dfs(i, visited):
        #         return True
        
        # return False
        
        # using Kahn's algorithm (BFS)
        
        queue = deque([])
        in_degree = [0]*V
        
        for node in range(V):
            for adj_node in adj[node]:
                in_degree[adj_node] += 1
                
        for node, deg in enumerate(in_degree):
            if deg == 0:
                queue.append(node)
           
        topo_sort = []     
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            
            for adj_node in adj[node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    queue.append(adj_node)
                    
        if len(topo_sort) != V:
            return True
        return False
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends