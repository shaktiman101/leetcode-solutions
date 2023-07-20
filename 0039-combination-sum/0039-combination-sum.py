class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def unique_comb(idx, k, tmp):
            if idx < 0 or k > target:
                return
            if k == target:
                res.append(tmp.copy())
                return
                
            # take
            k += candidates[idx]
            tmp.append(candidates[idx])
            unique_comb(idx, k, tmp)
            
            # not-take
            k -= candidates[idx]
            tmp.pop()
            unique_comb(idx-1, k, tmp)
        
        unique_comb(len(candidates)-1, 0, [])
        return res
        