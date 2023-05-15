class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # recursive approach
        # def func(nums, idx):
        #     if idx < 0:
        #         return 0
        #     take = nums[idx] + func(nums, idx-2)
        #     not_take = func(nums, idx-1)
        #     return max(take, not_take)
        # return func(nums, n-1)
    
    
        # memoization
        # dp = [-1]*n
#         def func(nums, idx):
#             if idx < 0:
#                 return 0
#             if dp[idx] != -1:
#                 return dp[idx]
#             take = nums[idx] + func(nums, idx-2)
#             not_take = func(nums, idx-1)
#             dp[idx] = max(take, not_take)
#             return dp[idx]
        
#         return func(nums, n-1)
        
        
        #tabulation
        dp = [0]*n
        dp[0] = nums[0]
        for idx in range(1, n):
            take = nums[idx]
            if idx > 1:
                take += dp[idx-2]
            not_take = dp[idx-1]
            dp[idx] = max(take, not_take)
        
        return dp[-1]
            
            
            