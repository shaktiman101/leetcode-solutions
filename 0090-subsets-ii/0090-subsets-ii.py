class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        def func(idx, cur):
            res.append(cur.copy())
            
            for i in range(idx, n):
                if i>idx and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                func(i+1, cur)
                cur.pop()
        
        func(0, [])
        return res