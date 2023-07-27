class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
#         def unique_comb(idx, k, tmp):
#             if idx < 0 or k > target:
#                 return
#             if k == target:
#                 res.append(tmp.copy())
#                 return
                
#             # take
#             k += candidates[idx]
#             tmp.append(candidates[idx])
#             unique_comb(idx, k, tmp)
            
#             # not-take
#             k -= candidates[idx]
#             tmp.pop()
#             unique_comb(idx-1, k, tmp)
        
#         unique_comb(len(candidates)-1, 0, [])
#         return res

#         def unique_comb(idx, target, tmp):
#             if idx < 0:
#                 if target == 0:
#                     res.append(tmp.copy())
#                 return
                
#             # take
#             if candidates[idx] <= target:
#                 target -= candidates[idx]
#                 tmp.append(candidates[idx])
#                 unique_comb(idx, target, tmp)
#                 target += candidates[idx]
#                 tmp.pop()
#             # else:
#             # not-take
#             unique_comb(idx-1, target, tmp)
        
#         unique_comb(len(candidates)-1, target, [])
#         return res

        # candidates.sort()
        def func(idx, tmp, target):
            if target < 0:
                return
            
            if target == 0:
                res.append(tmp.copy())
                return
                
            for i in range(idx, n):
                tmp.append(candidates[i])
                func(i, tmp, target-candidates[i])
                tmp.pop()
                
        func(0, [], target)
        return res
        