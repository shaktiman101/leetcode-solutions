class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        insertion_time = [float('inf')]*n
        lowest_ins_time = [float('inf')]*n
        visited = [False]*n
        bridge = []
        
        def dfs(node, parent, ins_count):
            visited[node] = True
            insertion_time[node] = ins_count
            lowest_ins_time[node] = ins_count
            
            for adj_node in adj[node]:
                if adj_node == parent:
                    continue
                
                if not visited[adj_node]:
                    dfs(adj_node, node, ins_count+1)
                    lowest_ins_time[node] = min(lowest_ins_time[adj_node], lowest_ins_time[node])
                    if lowest_ins_time[adj_node] > insertion_time[node]:
                        bridge.append((adj_node, node))
                else:
                    lowest_ins_time[node] = min(lowest_ins_time[adj_node], lowest_ins_time[node])
            
        ins_count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, -1, ins_count)
                
        return bridge
        
                