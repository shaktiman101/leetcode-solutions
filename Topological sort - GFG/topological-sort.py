from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # # DFS approach
        # visited = [False]*V
        # stack = []
        
        # def dfs(node):
        #     visited[node] = True
        #     for adj_node in adj[node]:
        #         if not visited[adj_node]:
        #             dfs(adj_node)
        #     stack.append(node)
            
        # for i in range(V):
        #     if not visited[i]:
        #         dfs(i)
        # topo_sort = stack[::-1]
        # return topo_sort
        
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
            
        return topo_sort
        
#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends