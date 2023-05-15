class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # recursive
        # def func(nums, idx):
        #     if idx < 0:
        #         return 0
        #     take = nums[idx] + func(nums, idx-2)
        #     not_take = func(nums, idx-1)
        #     return max(take, not_take)
        # first_skip = func(nums[1:], n-2)
        # last_skip = func(nums[:-1], n-2)
        
        # return max(first_skip, last_skip)
    
        # memoization
        def func(nums, idx):
            if idx < 0:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            take = nums[idx] + func(nums, idx-2)
            not_take = func(nums, idx-1)
            dp[idx] = max(take, not_take)
            return dp[idx]
            
        dp = [-1]*n
        first_skip = func(nums[1:], n-2)
        
        dp = [-1]*n
        last_skip = func(nums[:-1], n-2)
        return max(first_skip, last_skip)
        