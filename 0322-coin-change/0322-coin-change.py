class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        #recursive
        # def func(amount, idx):
        #     if amount < 0 or idx < 0:
        #         return float('inf')
        #     if amount == 0:
        #         return 0
        #     take = float('inf')
        #     if coins[idx] <= amount:
        #         take = 1 + func(amount-coins[idx], idx)
        #     not_take = func(amount, idx-1)
        #     return min(take, not_take)
        # ans = func(amount, n-1)
        # if ans == float('inf'):
        #     return -1
        # return ans
    
        #memoization
        dp = [[-1]*(n+1) for _ in range(amount+1)]
        def func(amount, idx):
            if amount < 0 or idx < 0:
                return float('inf')
            if amount == 0:
                return 0
            # print(amount, idx)
            if dp[amount][idx] != -1:
                return dp[amount][idx]
            take = float('inf')
            if coins[idx] <= amount:
                take = 1 + func(amount-coins[idx], idx)
            not_take = func(amount, idx-1)
            dp[amount][idx] = min(take, not_take)
            return dp[amount][idx]
        
        ans = func(amount, n-1)
        if ans == float('inf'):
            return -1
        return ans
            