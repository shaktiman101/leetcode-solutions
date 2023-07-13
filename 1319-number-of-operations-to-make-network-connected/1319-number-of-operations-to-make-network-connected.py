class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]
        
        def find_uparent(node):
            if node == parent[node]:
                return node
            parent[node] = find_uparent(parent[node])
            return parent[node]
        
        def union(u, v):
            pu = find_uparent(u)
            pv = find_uparent(v)
            if pu == pv:
                return 1
            
            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]
            return 0
        
        extra_conn = 0    
        for u, v in connections:
            extra_conn += union(u, v)
            
        total_comp = 0
        for node in range(n):
            if node == parent[node]:
                total_comp += 1
        
        # print(f"Total components = {comp}")
        # print(f"extra connections = {extra_conn}")
        # print(parent)
        connection_needed = total_comp-1
        if connection_needed <= extra_conn:
            return connection_needed
        return -1