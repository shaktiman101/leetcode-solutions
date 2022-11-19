from collections import deque
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(1, m):
            dp[i][0] = 1
        for j in range(1, n):
            dp[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                w1 = dp[i-1][j]
                w2 = dp[i][j-1]
                dp[i][j] = w1 + w2
        return dp[m-1][n-1]
                
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        
        def solve(left, up):
            if left < 0 or up < 0:
                return 0
            if left == 0 and up == 0:
                return 1
            if dp[left][up]:
                return dp[left][up]
            w1 = solve(left-1, up)
            w2 = solve(left, up-1)
            dp[left][up] = w1+w2
            return dp[left][up]
            
        solve(m-1, n-1)
        return dp[m-1][n-1]
        
#         dirs = [[0, 1], [1,0]]
#         q = deque([[0,0]])
#         visited = [[False]*n for _ in range(m)]
        
#         def is_valid(x, y):
#             if x < n and y < m:
#                 return True
#             return False
            
#         paths = 0
#         while q:
#             x, y = q.popleft()
#             if x == n-1 and y == m-1:
#                 paths += 1
                
#             for changex, changey in dirs:
#                 tmpx, tmpy = x + changex, y + changey
                
#                 if is_valid(tmpx, tmpy) and (not visited[tmpy][tmpx]):
#                     q.append([tmpx, tmpy])
#                     visited[tmpy][tmpx] = True
                    
#         return paths
                    