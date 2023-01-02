class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n, stack = len(graph), [0]
        visited = [False]*n
        
        paths = []
        def dfs(node, curr_path):
            # visited[node] = True
            # curr_path.append(node)
            if node == n-1:
                paths.append(curr_path.copy())
                    
            for adj_node in graph[node]:
                # if not visited[adj_node]:
                curr_path.append(adj_node)
                dfs(adj_node, curr_path)
                curr_path.pop()
            return
            
        dfs(0, [0])
        return paths
        
        
        
        
        def dfs(cur, path):
            if cur == len(graph) - 1: res.append(path)
            else:
                for i in graph[cur]: dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res
        