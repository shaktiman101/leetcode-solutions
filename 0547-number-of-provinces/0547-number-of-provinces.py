class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        edges = []
        # for node in range(V):
        #     for adj_node, is_connected  in enumerate(adj[node]):
        #         if is_connected and node != adj_node:
        #             edges.append((node, adj_node))
        for u in range(V):
            for v in range(V):
                if isConnected[u][v] and u != v:
                    edges.append((u,v))
                    
        print(edges)
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
            
        for node in range(V):       # to compress any remaining edges
            find_uparent(node)
            
        # provinces = 0
        # provinces_name= []
        # for i in range(V):
        #     if i == parent[i]:
        #         provinces += 1
        #         provinces_name.append(i)
        # print(set(parent))
        # print(provinces_name)
        # print(parent)
        # print(size)
        return len(set(parent))
        