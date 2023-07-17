class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        
        def func(idx, subset):
            if idx < 0:
                power_set.append(subset.copy())
                return
            
            subset.append(nums[idx])
            func(idx-1, subset)
            
            subset.pop()
            func(idx-1, subset)
        
        func(len(nums)-1, [])
        return power_set
        