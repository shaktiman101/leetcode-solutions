class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 == 1:
            return False
        target = total//2
        n = len(nums)
        
        dp = [[-1]*(target+1) for _ in range(n+1)]
        def func(n, target):
            if target == 0:
                if n == 0:
                    return True
                return False
            if target < 0 or n <= 0:
                return False
            if dp[n][target] != -1:
                return dp[n][target]
            
            dp[n][target] = func(n-1, target-nums[n-1]) or func(n-1, target)
            return dp[n][target]
        
        return func(n, target)
        
        
        
        target = sum(nums)
        if target%2 != 0:
            return False
        
        n = len(nums)
        def solve(n, target):
            if target is 0:
                return True
            if n < 1 or target < 0:
                return False
            
            return solve(n-1, target-nums[n-1]) or \
            solve(n-1, target)
        return solve(n, target//2)