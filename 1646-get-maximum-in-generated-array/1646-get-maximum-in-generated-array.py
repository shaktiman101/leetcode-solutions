class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        nums = [0]*(n+1)
        nums[1] = 1
        
        if n<3:
            return max(nums)       
        
        
        max_ = 0 #float('-inf')
        
        for i in range(1, n//2+1):
            if 2*i < n+1:
                nums[2*i] = nums[i]
                max_ = max(max_, nums[2*i])
                
            if 2*i < n:
                nums[2*i+1] = nums[i]+nums[i+1]
                max_ = max(max_, nums[2*i+1])
        
        return max_