class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        
        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = 0
                if diff in dp[j]:
                    cnt = dp[j][diff]
                    
                dp[i][diff] += cnt + 1
                ans += cnt
                
        return ans
#         count = 0
#         n = len(nums)
        
#         def func(n, tmp):
#             if n == 0:
#                 if len(tmp) > 2:
#                     diff = tmp[1]-tmp[0]
#                     flag = 0
#                     for i in range(2,len(tmp)):
#                         if tmp[i]-tmp[i-1] != diff:
#                             flag = 1
#                             break
#                     if flag == 0:
#                         nonlocal count
#                         count += 1
#                 return
#             func(n-1, tmp+[nums[n-1]])
#             func(n-1, tmp)
        
#         func(n, [])
#         return count    
        
#         n = len(nums)
#         count = 0
#         dp = [[0]*n for _ in range(n)]
        
#         def solve(i, tmp):
#             if i > n:
#                 return
#             if i == n:
#                 if len(tmp) > 2:
#                     nonlocal count
#                     count += 1
#                 return
#             if dp[i]:
                
#             if len(tmp) >= 2:
#                 diff = tmp[-1] - tmp[-2]
#                 if nums[i]-tmp[-1] == diff:
#                     tmp.append(nums[i])
#                     solve(i+1, tmp)
#                     tmp.pop()
#                     solve(i+1, tmp)
#                 else:
#                     solve(i+1, tmp)
#             else:
#                 tmp.append(nums[i])
#                 solve(i+1, tmp)
#                 tmp.pop()
#                 solve(i+1, tmp)
                
#         solve(0, [])
#         # print(res)
#         return count