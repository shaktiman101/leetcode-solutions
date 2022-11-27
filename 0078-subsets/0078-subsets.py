class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def solve(tmp, n):
            if n < 0:
                return
            if n == 0:
                ans.append(tmp.copy())
            solve(tmp+[nums[n-1]], n-1)
            solve(tmp, n-1)
        
        solve([], n)
        return ans
    
        # n = len(nums)
        # ans = [[]]
        # for i in range(n):
        #     tmp = []
        #     for subset in ans:
        #         subset2 = subset.copy()
        #         subset2.append(nums[i])
        #         tmp.append(subset2)
        #     ans.extend(tmp)
        # return ans
    
        ans = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return
            
            # decision to select ith index element in subet
            subset.append(nums[i])
            dfs(i+1)
            
            # decision to NOT select the ith index element
            subset.pop()
            dfs(i+1)
            
        
        # starting index of nums
        dfs(0)
        return ans
        
            