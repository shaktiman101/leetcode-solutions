#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        arr.sort()
        res = []
        visited = [False]*n
        
        def backtrack(tmp_size, tmp):
            if tmp_size == n:
                res.append(tmp.copy())
                return
            
            for i in range(n):
                if visited[i] or (i>0 and arr[i]==arr[i-1] and not visited[i-1]):
                    continue
                
                visited[i] = True
                tmp.append(arr[i])
                backtrack(tmp_size+1, tmp)
                tmp.pop()
                visited[i] = False
                
        backtrack(0, [])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends