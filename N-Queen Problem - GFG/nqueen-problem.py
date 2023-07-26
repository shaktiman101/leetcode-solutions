#User function Template for python3

class Solution:
    def nQueen(self, n):
        chessboard = [[0]*n for _ in range(n)]
        res = []
        
        def is_valid(x, y):
            if x<0 or y<0 or y>=n:
                return True
    
            for i in range(1,n):
                if x-i>=0 and chessboard[x-i][y] == 1:
                    return False
                if x-i>=0 and y-i>=0 and chessboard[x-i][y-i] == 1:
                    return False
                if x-i>=0 and y+i<n and chessboard[x-i][y+i] == 1:
                    return False
                    
            return True

        res = []
        def solve(cur):
            i, j = 0, 0
            while i < n:
                
                flag = 0
                while j < n:
                    
                    if is_valid(i, j):
                        chessboard[i][j] = 1
                        cur.append(j+1)
                        flag = 1
                        break
                    j += 1
                
                if flag == 0:
                    if not cur:
                        return res
                    j_prev = cur.pop()
                    chessboard[i-1][j_prev-1] = 0
                    j = j_prev
                    i -= 1
                elif len(cur) == n:
                    res.append(cur.copy())
                    j_prev = cur.pop()
                    chessboard[i][j_prev-1] = 0
                    j = j_prev
                else:
                    i += 1
                    j = 0
        solve([])
        return res

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends