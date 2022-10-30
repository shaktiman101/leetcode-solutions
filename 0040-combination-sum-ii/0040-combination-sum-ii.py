class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         ans, subset = [], []
#         nums = candidates
#         nums.sort()
        
#         def backtrack(i, total):
#             if total == target:
#                 ans.append(subset.copy())
#                 return
#             if i == len(nums) or total > target:
#                 return
            
#             subset.append(nums[i])
#             total += nums[i]
#             backtrack(i+1, total)
            
#             tmp = subset.pop()
#             total -= tmp
#             while i+1 < len(nums) and nums[i] == nums[i+1]:
#                 i += 1
#             backtrack(i+1, total)
        
#         backtrack(0, 0)
#         return ans

        candidates = sorted(candidates)
        res = set()
        i, n = 0, len(candidates)
        def solve(i, target, tmp):
            if target == 0:
                res.add(tuple(tmp))
            if target < 0 or i >= n:
                return
            
            target -= candidates[i]
            tmp.append(candidates[i])
            solve(i+1, target, tmp)
            
            while i < n-1 and candidates[i] == candidates[i+1]:
                i += 1
            target += tmp.pop() #candidates[i]
            
            solve(i+1, target, tmp)

        solve(0, target, [])
        return res