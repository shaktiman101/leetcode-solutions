class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # recursive approach
        # TC: O(2^N)
        # SC: O(N) heap stack space
#         def rob(st_idx, cur_idx):
#             if cur_idx < st_idx:
#                 return 0
#             take = nums[cur_idx] + rob(st_idx, cur_idx-2)
#             not_take = rob(st_idx, cur_idx-1)
#             return max(take, not_take)
            
#         return max(rob(0, n-2), rob(1, n-1))
        
        # memoized approach
        # TC: O(N)
        # SC: O(N) heap stack space + O(N) array space
#         def rob(st_idx, cur_idx, dp):
#             if cur_idx < st_idx:
#                 return 0
#             if dp[cur_idx] != -1:
#                 dp[cur_idx]
                
#             take = nums[cur_idx] + rob(st_idx, cur_idx-2, dp)
#             not_take = rob(st_idx, cur_idx-1, dp)
#             dp[cur_idx] = max(take, not_take)
#             return dp[cur_idx]
            
#         return max(rob(0, n-2, [-1]*n), rob(1, n-1, [-1]*n))
    
    
        # tabulation
        # TC: O(2N)
        # SC: O(2N) array space
        # def rob(dp, st_idx, end_idx):
        def rob(nums):
            n = len(nums)
            dp = [0]*n
            st_idx, end_idx = 0, n-1
            dp[st_idx] = nums[st_idx]
            
            for i in range(st_idx+1, end_idx+1):
                take = nums[i] 
                if i-2 >= 0:
                    take += dp[i-2]
                not_take = dp[i-1]
                dp[i] = max(take, not_take)
            
            return dp[end_idx]
            
        # return max(rob([0]*n, 0, n-2), rob([0]*n, 1, n-1))
        return max(rob(nums[1:]), rob(nums[:-1]) )
    
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
#         def func(nums, idx):
#             if idx < 0:
#                 return 0
#             if dp[idx] != -1:
#                 return dp[idx]
#             take = nums[idx] + func(nums, idx-2)
#             not_take = func(nums, idx-1)
#             dp[idx] = max(take, not_take)
#             return dp[idx]
            
#         dp = [-1]*n
#         first_skip = func(nums[1:], n-2)
        
#         dp = [-1]*n
#         last_skip = func(nums[:-1], n-2)
#         return max(first_skip, last_skip)
    
    
        # tabulation
        def func(nums):
            n = len(nums)
            dp = [0]*n
            dp[0] = nums[0]
            for idx in range(1, n):
                take = nums[idx] 
                if idx > 1:
                    take += dp[idx-2]
                not_take = dp[idx-1]
                dp[idx] = max(take, not_take)
            return dp[-1]
        return max(func(nums[1:]), func(nums[:-1]))
        