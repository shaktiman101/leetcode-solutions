#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        # recursive approach
        # TC: O(2^N), SC: O(N) stack heap space
        # def func(stair):
        #     if stair > n:
        #         return 0
        #     if stair == n:
        #         return 1
            
        #     n1_ways =  func(stair+1) 
        #     n2_ways =  func(stair+2)
        #     return n1_ways+n2_ways
            
        # return func(0)
        
        # memoized approach
        # TC: O(N), SC: O(N) for dp array & O(N) for stack space
        dp = [-1]*(n+1)
        mod = int(1e9)+7
        def func(stair):
            if stair > n:
                return 0
            if stair == n:
                return 1
            if dp[stair] != -1:
                return dp[stair]
                
            n1_ways =  func(stair+1) 
            n2_ways =  func(stair+2)
            dp[stair] = (n1_ways+n2_ways)%mod
            return dp[stair]
            
        return func(0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends