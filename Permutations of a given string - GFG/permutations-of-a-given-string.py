#User function Template for python3

class Solution:
    def find_permutation(self, S):
        arr = list(S)
        n = len(arr)
        res = set()
        
        def solve(arr, tmp, visited):
            if len(visited) == n:
                res.add(''.join(tmp))
                return
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    solve(arr, tmp+[arr[i]], visited)
                    visited.remove(i)
            
        solve(arr, [], set())
        return sorted(res)
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends