class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        
        def dfs(node,par):
            
            res = 0
            for nei in tree[node]:
                if nei != par:
                    res += dfs(nei,node)
            
            if res or hasApple[node]:
                return res + 2

            return res

        return max(dfs(0,-1)-2, 0)
        
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        total_apples = sum(hasApple)
        def func(node, total_apples, time_taken):
            if total_apples == 0:
                return time_taken
            
            tmp = [float('inf')]*len(adj_list[node])
            for adj_node in adj_list[node]:
                if hasApple[adj_node]:
                    tmp[adj_node] = func(adj_node, total_apples-1, time_taken+1)
                else:
                    tmp[adj_node] = func(adj_node, total_apples, time_taken+1)
            return min(tmp)
        
        func(0, total_apples, 0)
                