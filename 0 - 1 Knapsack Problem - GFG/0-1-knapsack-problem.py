#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        memo = [[-1]*(W+1) for _ in range(n+1)]
        def func(W, idx):
            if idx == 0:
                if wt[0] <= W:
                    return val[0]
                return 0
            if memo[idx][W] != -1:
                return memo[idx][W]
            val1 = float('-inf')
            if wt[idx] <= W:
                val1 = val[idx] + func(W-wt[idx], idx-1)
            val2 = func(W, idx-1)
            memo[idx][W] = max(val1, val2)
            return memo[idx][W]
        
        return func(W, n-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends