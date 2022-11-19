from collections import deque
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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
        
        dirs = [[0, 1], [1,0]]
        q = deque([[0,0]])
        visited = [[False]*n for _ in range(m)]
        
        def is_valid(x, y):
            if x < n and y < m:
                return True
            return False
            
        paths = 0
        while q:
            x, y = q.popleft()
            if x == n-1 and y == m-1:
                paths += 1
                
            for changex, changey in dirs:
                tmpx, tmpy = x + changex, y + changey
                
                if is_valid(tmpx, tmpy) and (not visited[tmpy][tmpx]):
                    q.append([tmpx, tmpy])
                    visited[tmpy][tmpx] = True
                    
        return paths
                    