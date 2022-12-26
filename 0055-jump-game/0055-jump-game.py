class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # max_index_reachable = 0
        # for curr_idx, max_jump_allowed in enumerate(nums):
        #     if max_index_reachable >= n-1:
        #         return True
        #     if curr_idx > max_index_reachable:
        #         return False
        #     max_index_reachable = max(max_index_reachable, curr_idx+max_jump_allowed)
        # return True
    
        # tabulation
        n = len(nums)
        dp = [False]*n
        dp[n-1] = True
        
        for i in range(n-2, -1, -1):
            for j in range(1, nums[i]+1):
                if i+j < n and dp[i+j]:
                    dp[i] = True
                    break
        return dp[0]
    
        # memoization
        n = len(nums)
        dp = [-1]*n
        def func(i):
            if i >= n:
                return False
            if i == n-1:
                return True
            if dp[i] != -1:
                return dp[i]
            
            for j in range(1,nums[i]+1):
                if func(i+j):
                    dp[i] = True
                    return dp[i]
            dp[i] = False
            return dp[i]
            
        return func(0)
        
        
        # SC: recursive stack space
        # TC: exponential, 1e5**n
        n = len(nums)
        def func(i):
            if i >= n:
                return False
            if i == n-1:
                return True
            for j in range(1,nums[i]+1):
                if func(i+j):
                    return True
            return False
            
        return func(0)