class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0]*(n+1)
        def num_ways(n):
            if n<=1 :
                return 1
            if dp[n]:
                return dp[n]
            dp[n] =num_ways(n-1)+num_ways(n-2)
            return dp[n]

        return num_ways(n)