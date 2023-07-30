#User function Template for python3

from typing import List
from collections import deque

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # safe_nodes = []
        # visited = [False]*V
        # path_visited = [False]*V
        # check = [0]*V
        
        # def dfs(node, path_visited, check):
        #     visited[node] = True
        #     path_visited[node] = True
        #     check[node] = 0
            
        #     for adj_node in adj[node]:
        #         if not visited[adj_node]:
        #             if dfs(adj_node, path_visited, check):
        #                 check[node] = 0
        #                 return True
                        
        #         elif path_visited[adj_node]:
        #             check[node] = 0
        #             return True
                    
        #     check[node] = 1
        #     path_visited[node] = False
        #     return False
            
        # for i in range(V):
        #     if not visited[i]:
        #         dfs(i, path_visited, check)
                
        
        # for i in range(V):
        #     if check[i]==1:
        #         safe_nodes.append(i)
                
        # return safe_nodes
        rev_adj = [[] for _ in range(V)]
        in_degree = [0]*V
        
        for node in range(V):
            for adj_node in adj[node]:
                rev_adj[adj_node].append(node)
                in_degree[node] += 1
                
        queue = deque([])
        for node, in_deg in enumerate(in_degree):
            if in_deg == 0:
                queue.append(node)
        
        res = []        
        while queue:
            node = queue.popleft()
            res.append(node)
            
            for adj_node in rev_adj[node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    queue.append(adj_node)
                    
        return sorted(res)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends