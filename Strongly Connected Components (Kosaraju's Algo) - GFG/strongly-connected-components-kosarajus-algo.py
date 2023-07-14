#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # sort nodes in order of finishing time
        node_fin_time = []
        visited = [False]*V
        
        def dfs(node):
            visited[node] = True
            for adj_node in adj[node]:
                if not visited[adj_node]:
                    dfs(adj_node)
            node_fin_time.append(node)
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
        # print(node_fin_time)
        
        # reverse the graph
        rev_adj = [[] for _ in range(V)]
        for node in range(V):
            for adj_node in adj[node]:
                rev_adj[adj_node].append(node)
                
        
        visited = [False]*V
        scc = 0
        while node_fin_time:
            node = node_fin_time.pop()
            if not visited[node]:
                stack = [node]
                scc += 1
                
                while stack:
                    curr_node = stack.pop()
                    visited[curr_node] = True
                    
                    for adj_node in rev_adj[curr_node]:
                        if not visited[adj_node]:
                            stack.append(adj_node)
                
        return scc

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
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
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends