class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [False]*n
        stack = [source]
        while stack:
            node = stack.pop()
            visited[node] = True
            if node == destination:
                return True
            for adj_node in adj_list[node]:
                if not visited[adj_node]:
                    stack.append(adj_node)
        return False
                
            
        