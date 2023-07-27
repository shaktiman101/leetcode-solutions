#User function Template for python3

class Solution:
    def findPath(self, m, n):
        if m[0][0] == 0:
            return []
            
        res = []
        dirs = [(0,1,'R'),(1,0,'D'),(0,-1,'L'),(-1,0,'U')]
        visited = [[False]*n for _ in range(n)]
        
        
        def is_valid(x, y):
            if x>=0 and x<n and y>=0 and y<n and m[x][y] == 1:
                return True
            return False
            
            
        def backtrack(x, y, tmp):
            if x==n-1 and y==n-1:
                res.append(''.join(tmp))
                return
            
            for delx, dely, dir_ in dirs:
                changedx, changedy = x+delx, y+dely
                if is_valid(changedx, changedy) and not visited[changedx][changedy]:
                    visited[changedx][changedy] = True
                    tmp.append(dir_)
                    backtrack(changedx, changedy, tmp)                    
                    tmp.pop()
                    visited[changedx][changedy] = False
                    
        visited[0][0] = True
        backtrack(0,0, [])
        
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends