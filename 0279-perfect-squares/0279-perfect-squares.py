import math
class Solution:
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
    
    def numSquares2(self, n: int) -> int:
        count = 0
        # perfect_squares = [{} for i in range(1, 101)]
        
        def func(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            
            sqrt = math.floor(n **0.5)
            n1 = 1+func(n-sqrt**2)
            
            n2 = float('inf')
            if sqrt > 1:
                n2 = 1+func(n- (sqrt-1)**2)
            return min(n1, n2)
        return func(n)
        