#User function Template for python3

class Solution:
    def subsets(self, A):
        res = []
        n = len(A)
        # A.sort()
        
        def func(idx, subset):
            res.append(subset.copy())
            
            for i in range(idx, n):
                
                subset.append(A[i])
                func(i+1, subset)
                subset.pop()
                
        func(0, [])
        return sorted(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends