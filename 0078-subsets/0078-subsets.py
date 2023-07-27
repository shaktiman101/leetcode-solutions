class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        n = len(nums)
        
#         def func(idx, subset):
#             if idx < 0:
#                 power_set.append(subset.copy())
#                 return
            
#             subset.append(nums[idx])
#             func(idx-1, subset)
            
#             subset.pop()
#             func(idx-1, subset)
        
#         func(len(nums)-1, [])
#         return power_set

        def func(idx, subset):
            power_set.append(subset.copy())
            
            for i in range(idx, n):
                subset.append(nums[i])
                func(i+1, subset)
                subset.pop()
                
        func(0, [])
        return power_set
        