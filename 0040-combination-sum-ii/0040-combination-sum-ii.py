class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        
        def func(idx, tmp, target):
            if target < 0:
                return
            
            if target == 0:
                res.append(tmp.copy())
                return
                
            for i in range(idx, n):
                if i>idx and candidates[i] == candidates[i-1]:
                    continue
                    
                tmp.append(candidates[i])
                func(i+1, tmp, target-candidates[i])
                tmp.pop()
                
        func(0, [], target)
        return res