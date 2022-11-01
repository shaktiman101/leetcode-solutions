class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         ans, subset = set(), []
#         nums.sort()
        
#         def dfs(i):
#             if i >= len(nums):
#                 if tuple(subset) not in ans:
#                     ans.add(tuple(subset.copy()))
#                 return
            
#             subset.append(nums[i])
#             dfs(i+1)
            
#             if subset:
#                 subset.pop()
#             dfs(i+1)
        
#         dfs(0)
#         return ans

        # second approach
#         ans, subset = [], []
#         nums.sort()
        
#         def dfs(i):
#             if i >= len(nums):
#                 ans.append(subset.copy())
#                 return
            
#             subset.append(nums[i])
#             dfs(i+1)
            
#             subset.pop()
#             while i+1 < len(nums) and nums[i] == nums[i+1]:
#                 i += 1
#             dfs(i+1)
        
#         dfs(0)
#         return ans
    
#         ans, subset = [], []
#         nums.sort()
        
#         def dfs(start):
#             # if start == len(nums):
#             ans.append(subset[:])
#                 # return
            
#             for i in range(start, len(nums)):
#                 if i > start and nums[i] == nums[i-1]:
#                     continue
#                 subset.append(nums[i])
#                 dfs(i+1)
#                 subset.pop()
        
#         dfs(0)
#         return ans

        nums = sorted(nums)
        res, n = [], len(nums)
        def solve(idx, subset):
            # if n < 1:
            res.append(subset)
                # return
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                solve(i+1, subset+[nums[i]])
                
        solve(0, [])
        return res
        