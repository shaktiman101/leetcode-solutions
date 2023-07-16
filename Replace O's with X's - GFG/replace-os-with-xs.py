#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = [[False]*m for _ in range(n)]
        res = [['X']*m for _ in range(n)]
                
            
        def dfs(x, y):
            res[x][y] = 'O'
            visited[x][y] = True
            
            for delx, dely in dirs:
                tmpx, tmpy = x+delx, y+dely 
                if tmpx>=0 and tmpx<n and tmpy>=0 and tmpy<m and \
                mat[tmpx][tmpy]=='O' and not visited[tmpx][tmpy]:
                    dfs(tmpx, tmpy)
            
            
        for row in [0,n-1]:
            for col in range(m):
                if not visited[row][col] and mat[row][col] == 'O':
                    dfs(row, col)
                    
        for row in range(n):
            for col in [0, m-1]:
                if not visited[row][col] and mat[row][col] == 'O':
                    dfs(row, col)
                                
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends