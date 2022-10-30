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

#         candidates = sorted(candidates)                 # TC: O(nlog(n))
#         res = []
#         i, n = 0, len(candidates)
#         def solve(i, target, tmp):                      # TC: O(2**n)
#             if target == 0:
#                 res.append(tmp.copy())                  # TC: O(k)   -> k = avg. size of tmp list
#             if target < 0 or i >= n:
#                 return
            
#             target -= candidates[i]
#             tmp.append(candidates[i])
#             solve(i+1, target, tmp)
            
#             while i < n-1 and \                         # TC: O(t) -> t = avg. duplicate elements
#             candidates[i] == candidates[i+1]:     
#                 i += 1
#             target += tmp.pop() #candidates[i]
            
#             solve(i+1, target, tmp)

#         solve(0, target, [])
#         return res
    
#         # overall TC: O(nlogn) + O(2**n *(k+t))

        candidates = sorted(candidates)
        res, n = [], len(candidates)
        
        def solve(idx, target, tmp):
            if target == 0:
                res.append(tmp)
            # if target < 0 or i >= n or candidates[i] > target:
            #     return
            
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                solve(i+1, target-candidates[i], tmp+[candidates[i]])
            
        solve(0, target, [])
        return res
        