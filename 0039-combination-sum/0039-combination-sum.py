class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         ans = []
#         subset = []
        
#         def dfs(i, target):
#             if i >= len(candidates) or target < 0:
#                 return
#             if target == 0:
#                 ans.append(subset.copy())
#                 return
            
#             subset.append(candidates[i])
#             target -= candidates[i]
#             dfs(i, target)
            
#             tmp = subset.pop()
#             target += tmp
#             dfs(i+1, target)
            
#         dfs(0, target)
#         return ans

        res = []
        def solve(n, tmp, sum_):
            
            if sum_ == target:
                res.append(tmp.copy())
                return
            if sum_ > target:
                return
            if n<1:
                return
            tmp.append(candidates[n-1])
            sum_ += candidates[n-1]
            solve(n, tmp, sum_)
            
            tmp.remove(candidates[n-1])
            sum_ -= candidates[n-1]
            solve(n-1, tmp, sum_)
            
        solve(len(candidates), [], 0)
        return res