from collections import deque
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        N = n
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        return res

        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # visited = [False]*n
        # dist_dp = [[-1]*n for _ in range(n
        
        def dfs(node, dist, visited):
            visited[node] = True
            # dist_sum += dist
            for adj_node in adj_list[node]:
                if not visited[adj_node]:
                    return dist+dfs(adj_node, dist+1, visited)
            return dist
            
        ans = [0]*n
        for i in range(n):
            # if not visited[i]:
            visited = [False]*n
            dist = dfs(i, 0, visited)
            ans[i] = dist
        return ans