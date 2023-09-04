class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        
        n = len(nums)
#         def func(idx, target):
#             if target < 0:
#                 return False
#             if idx==0:
#                 if nums[0] == target or target == 0:
#                     return True
#                 return False
            
#             take = func(idx-1, target-nums[idx])
#             not_take = func(idx-1, target)
#             return take or not_take
        
#         return func(n-1, total//2)
        target = total//2
        dp = [[-1]*(target+1) for _ in range(n)]
        def func(idx, target):
            if target < 0:
                return False
            if idx==0:
                if nums[0] == target or target == 0:
                    return True
                return False
            if dp[idx][target] != -1:
                return dp[idx][target]
            
            take = func(idx-1, target-nums[idx])
            not_take = func(idx-1, target)
            
            dp[idx][target] = take or not_take
            return dp[idx][target]
        
        return func(n-1, target)