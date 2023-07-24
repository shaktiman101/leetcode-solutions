class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False]*n
        res = []
        
        def func(tmp_size, tmp, visited):
            if tmp_size == n:
                res.append(tmp.copy())
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                    
                tmp.append(nums[i])
                visited[i] = True
                func(tmp_size+1, tmp, visited)
                visited[i] = False
                tmp.pop()
        
        func(0, [], visited)
        return res