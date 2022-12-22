from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, count = len(isConnected), 0
        visited = [False]*n
        def dfs(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)
        
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        return count
            
        n, count = len(isConnected), 0
        visited = [False]*n
        
        for i in range(n):
            if not visited[i]:
                count += 1
                # q = deque([i])
                stack = [i]
                
                while stack:
                    # city = q.popleft()
                    city = stack.pop()
                    visited[city] = True
                    for adj_city in range(n):
                        if isConnected[city][adj_city] == 1 and not visited[adj_city]:
                            # q.append(adj_city)
                            stack.append(adj_city)
        return count
        