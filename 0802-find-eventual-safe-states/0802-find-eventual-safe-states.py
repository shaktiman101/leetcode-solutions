class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = graph
        V = len(adj)
        safe_nodes = []
        visited = [False]*V
        path_visited = [False]*V
        check = [0]*V
        
        def dfs(node, path_visited, check):
            visited[node] = True
            path_visited[node] = True
            check[node] = 0
            
            for adj_node in adj[node]:
                if not visited[adj_node]:
                    if dfs(adj_node, path_visited, check):
                        check[node] = 0
                        return True
                        
                elif path_visited[adj_node]:
                    check[node] = 0
                    return True
                    
            check[node] = 1
            path_visited[node] = False
            return False
            
        for i in range(V):
            if not visited[i]:
                dfs(i, path_visited, check)
                
        
        for i in range(V):
            if check[i]==1:
                safe_nodes.append(i)
                
        return safe_nodes