class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom-up solution
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        
        for i in range(1,n):
            rob = nums[i]
            if i > 1:
                rob += dp[i-2]
            not_rob = dp[i-1]
            dp[i] = max(rob, not_rob)
        
        return dp[n-1]
        
        
        # top-down: memoization
        n = len(nums)
        dp = [0]*n
        def solve(idx):
            if idx < 0:
                return 0
            if dp[idx]:
                return dp[idx]
            rob = nums[idx] 
            if idx > 1:
                rob += solve(idx-2)
            not_rob = solve(idx-1)
            dp[idx] = max(rob, not_rob)
            return dp[idx]
        
        return solve(n-1)
    
    
        # recursive solution
        n = len(nums)
        def solve(idx):
            if idx < 0:
                return 0
            rob = nums[idx] 
            if idx > 1:
                rob += solve(idx-2)
            not_rob = solve(idx-1)
            return max(rob, not_rob)
        return solve(n-1)
        
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        
#         # recursive + memoization approach
#         memo = [None]*n
#         def solve(nums, n):
#             if n < 0:
#                 return 0
            
#             if memo[n] != None:
#                 return memo[n]
                
#             rob = nums[n] + solve(nums, n-2)
#             dont_rob = solve(nums, n-1)
                
#             memo[n] = max(rob, dont_rob)
#             return memo[n]
        
#         return solve(nums, n-1)

        # iterative + memoization approach
#         memo = [0, nums[0]]
#         for i in range(1, n):
#             memo.append(max(memo[i], memo[i-1] + nums[i]))
            
#         return memo[-1]
    
        
        