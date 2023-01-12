from collections import deque, defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node: int):
            cnt = Counter()
            if node not in seen:
                cnt[labels[node]] += 1 
                seen.add(node)
                for child in g.get(node, []):
                    cnt += dfs(child)
                ans[node] = cnt[labels[node]]
            return cnt
        
        g, ans, seen = defaultdict(list), [0] * n, set()
        for a, b in edges:
            g[a] += [b]
            g[b] += [a]
        dfs(0)
        return ans
    
    
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        stack = [0]
        visited = [False]*n
        label_node = defaultdict(list)
        while stack:
            node = stack.pop()
            label = labels[node]
            label_node[label].append(node)
            visited[node] = True
            
            for adj_node in adj_list[node]:
                if not visited[adj_node]:
                    stack.append(adj_node)
        
        ans = [0]*n
        for label, nodes in label_node.items():
            k = len(nodes)
            for node in nodes:
                ans[node] = k
                k -= 1
        return ans
                