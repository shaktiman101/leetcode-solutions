class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        i, n, ice_cream = 0, len(costs), 0
        
        while coins and i < n:
            if costs[i] <= coins:
                ice_cream += 1
                coins -= costs[i]
                i += 1
            else:
                return ice_cream
        return ice_cream
                
        
        n = len(costs)
        dp = [[0]*(coins+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, coins+1):
                not_take = 0+dp[i-1][j] #, ice_cream)
                take = 0
                if costs[i-1] <= j:
                    take = 1+dp[i-1][j-costs[i-1]] #, ice_cream)
                ice_cream = max(not_take, take) 
                dp[i][j] = ice_cream
        return dp[n][coins]
    
    
        
        n = len(costs)
        dp = [[-1]*(coins+1) for _ in range(n+1)]
        def func(n, coins, ice_cream):
            if n < 1 or coins == 0 :
                return ice_cream
            if dp[n][coins] != -1:
                return dp[n][coins]
            not_take = 0+func(n-1, coins, ice_cream)
            take = 0
            if costs[n-1] <= coins:
                take = 1+func(n-1, coins-costs[n-1], ice_cream)
            ice_cream = max(not_take, take) 
            dp[n][coins] = ice_cream
            return dp[n][coins]
        
        return func(n, coins, 0)
    
    
        n = len(costs)
        def func(n, coins, ice_cream):
            if n < 1 or coins == 0 :
                return ice_cream
            
            not_take = 0+func(n-1, coins, ice_cream)
            take = 0
            if costs[n-1] <= coins:
                take = 1+func(n-1, coins-costs[n-1], ice_cream)
            ice_cream = max(not_take, take) 
            return ice_cream
        
        return func(n, coins, 0)