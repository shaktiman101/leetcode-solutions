#User function Template for python3

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        
        edges = []
        for node in range(V):
            for adj_node, adj_weight in adj[node]:
                edges.append((adj_weight, node, adj_node))
        
        edges = sorted(edges, key=lambda x: x[0])
        
        parent = [i for i in range(V)]
        size = [1 for _ in range(V)]
        
        # mst_edges = []
        mst_weight = 0
        
        def find_uparent(node):
            if node == parent[node]:
                return node
            parent[node] = find_uparent(parent[node])
            return parent[node]
    
        def union(u, v):
            pu = find_uparent(u)
            pv = find_uparent(v)
            if pu == pv:
                return
            
            nonlocal mst_weight
            mst_weight += weight
            
            # nonlocal mst_edges
            # mst_edges.append((u, v))
            if size[pu] > size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]
            
        for weight, u, v in edges:
            union(u, v)
        
        return mst_weight


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends