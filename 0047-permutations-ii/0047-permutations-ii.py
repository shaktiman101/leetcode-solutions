class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        visited = [False]*n
        res = []
        
        def func(tmp_size, tmp, visited, idx):
            if tmp_size == n:
                res.append(tmp.copy())
                return
            
            for i in range(n):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                    
                tmp.append(nums[i])
                visited[i] = True
                func(tmp_size+1, tmp, visited, i+1)
                visited[i] = False
                tmp.pop()
        
        func(0, [], visited, 0)
        return res