class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2 == 0:
            return True
        return False
    
        if n == 1:
            return False
        if n == 2:
            return True
        
        def get_divisor(n):
            divisor = [1]
            for i in range(2, n//2):
                if n%i == 0:
                    divisor.append(i)
                    if i != n//i:
                        divisor.append(i)
            return divisor
            
        # 1-Alice, 0-Bob
        dp = [-1]*(n+1)
        def func(n, player):
            if n == 1:
                if player:
                    return False
                return True
            
            if dp[n] != -1:
                return dp[n]
            
            for div in get_divisor(n):
                dp[n] = func(n-div, 1-player)
                return dp[n]
        
        return func(n, 1)
            
            