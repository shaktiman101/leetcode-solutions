#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        edges = []
        for node in range(V):
            for adj_node, is_connected  in enumerate(adj[node]):
                if is_connected and node != adj_node:
                    edges.append((node, adj_node))
        
        # print(edges)
        parent= [i for i in range(V)]
        size = [1 for _ in range(V)]
        
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
            
            if size[pu] > size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]
            
        for u, v in edges:
            union(u, v)
            
        provinces = 0
        for i in range(V):
            if i == parent[i]:
                provinces += 1
        return provinces


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends