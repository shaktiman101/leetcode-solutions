class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        answer = [-1]*n
        
        for j in range(n):
            stack = [(0, j)]
            while stack:
                row, col = stack.pop()
                if row == m:
                    answer[j] = col
                    break
                if col==0 and grid[row][col]==-1:
                    break
                elif col==n-1 and grid[row][col]==1:
                    break
                if grid[row][col] == 1 and grid[row][col+1] == -1:
                    break
                if grid[row][col] == -1 and grid[row][col-1] == 1:
                    break
                stack.append((row+1, col+grid[row][col]))
        return answer
            