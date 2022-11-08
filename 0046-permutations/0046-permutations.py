class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
#         def solve(nums, tmp, visited):
#             if len(visited) == n:
#                 res.append(tmp)
#                 return
            
#             for i in range(n):
#                 if i not in visited:
#                     visited.add(i)
#                     solve(nums, tmp+[nums[i]], visited)
#                     visited.remove(i)
        
#         solve(nums, [], set())
#         return res

        def solve2(nums, idx):
            if idx == n:
                res.append(nums.copy())
                return
            
            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                solve2(nums, idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]
        
        solve2(nums, 0)
        return res
                