#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # disjoint set | union ds
        # edges = []
        # for node in range(V):
        #     for adj_node, is_connected  in enumerate(adj[node]):
        #         if is_connected and node != adj_node:
        #             edges.append((node, adj_node))
        
        # # print(edges)
        # parent= [i for i in range(V)]
        # size = [1 for _ in range(V)]
        
        # def find_uparent(node):
        #     if node == parent[node]:
        #         return node
        #     parent[node] = find_uparent(parent[node])
        #     return parent[node]
            
        # def union(u, v):
        #     pu = find_uparent(u)
        #     pv = find_uparent(v)
        #     if pu == pv:
        #         return
            
        #     if size[pu] > size[pv]:
        #         parent[pv] = pu
        #         size[pu] += size[pv]
        #     else:
        #         parent[pu] = pv
        #         size[pv] += size[pu]
            
        # for u, v in edges:
        #     union(u, v)
            
        # provinces = 0
        # provinces_name= []
        # for i in range(V):
        #     if i == parent[i]:
        #         provinces += 1
        #         provinces_name.append(i)
        # print(set(parent))
        # print(provinces_name)
        # print(parent)
        # return provinces_name #len(set(parent))
        
        adj_list = [[] for _ in range(V)]
        for node in range(V):
            for adj_node, is_connected in enumerate(adj[node]):
                if is_connected and node != adj_node:
                    adj_list[node].append(adj_node)
                    
        visited = [False]*V
        provinces = 0
        for node in range(V):
            if not visited[node]:
                    stack = [node]
                    provinces += 1
                    
                    while stack:
                        node = stack.pop()
                        visited[node] = True
                        
                        for adj_node in adj_list[node]:
                            if not visited[adj_node]:
                                stack.append(adj_node)
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