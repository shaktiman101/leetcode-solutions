from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        m,n = len(board),len(board[0])
        
        def backtrack(i,j,k,visited):
            if board[i][j] == word[k]:
                if k==len(word)-1:
                    return True
                
                for xn,yn in directions:
                    x,y = i+xn,j+yn
                    if 0<=x<m and 0<=y<n and (x,y) not in visited:
                        visited.add((x,y))                      # Change the state
                        if backtrack(x,y,k+1,visited)==True:    # Recursive call
                            return True
                        visited.remove((x,y))                   # Restore the state
            return False
        
        # start from each cell in the grid.
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0,{(i,j)}):
                    return True
        return False
        
        
#         m, n = len(board), len(board[0])
#         dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        
#         def is_valid(tmpx, tmpy, k):
#             if tmpx >= 0 and tmpx < m and tmpy >=0 and tmpy < n and \
#             board[tmpx][tmpy] == word[k]:
#                 return True
#             return False
        
#         visited = set()
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == word[0]:
#                     q = deque([(i, j)])
#                     visited.clear()
#                     visited.add((i, j))
#                     k = 0
                    
#                     while q and k < len(word):
#                         x, y = q.popleft()
#                         k += 1
#                         if k == len(word):
#                             return True
#                         flag = 0
#                         for changex, changey in dirs:
#                             tmpx, tmpy = x+changex, y+changey
                            
#                             if is_valid(tmpx, tmpy, k) and (not (tmpx, tmpy) in visited):
#                                 q.append((tmpx, tmpy))
#                                 visited.add((tmpx, tmpy))
#                                 flag = 1
#                         if flag == 0:
#                             k -= 1
#                     if k == len(word):
#                         return True
#         return False
                                
                    
        