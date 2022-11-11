class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom-up: TC: O(n); SC: O(1)
        if len(nums) == 1:
            return nums[0]
        def func(nums):
            n = len(nums)
            prev2, prev = 0, nums[0]
            for i in range(1,n):
                rob = nums[i]
                if i > 1:
                    rob += prev2
                not_rob = prev
                curr = max(rob, not_rob)
                prev2, prev = prev, curr
            return prev
        
        return max(func(nums[1:]), func(nums[:-1]))
    
    
        # memoization
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def solve(nums, idx):
            if idx == 0:
                return nums[0]
            if dp[idx]:
                return dp[idx]
            take = nums[idx] 
            if idx > 1:
                take += solve(nums, idx-2)
            not_take = solve(nums, idx-1)
            dp[idx] = max(take, not_take)
            return dp[idx]
        
        dp = [0]*(n-1)
        # dp[0] = nums[1]
        solve(nums[1:], n-2)
        ans1 = dp[-1]
        print(dp)
        
        solve(nums[:-1], n-2)
        ans2 = dp[-1]
        print(dp)
        return max(ans1, ans2)
    
        
        # recursive solution
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def solve(nums, idx):
            if idx == 0:
                return nums[0]
            take = nums[idx] 
            if idx > 1:
                take += solve(nums, idx-2)
            not_take = solve(nums, idx-1)
            return max(take, not_take)
        
        return max(solve(nums[1:], n-2), solve(nums[:-1], n-2))
        
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        memo = [0]*(n+1)
        memo[1] = nums[0]
        # memo[2] = max(nums[:2])
        for i in range(1, n):
            memo.append(max(memo[i], memo[i-1] + nums[i]))
            
        return memo[-1]
        