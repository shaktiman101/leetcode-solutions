class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans, stack = [0]*n, []
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]-i
            stack.append(i)
        return ans
            
            
        
        
#         T = temperatures
#         ans = [0] * len(T)
#         stack = []
#         for i, t in enumerate(T):
#             while stack and T[stack[-1]] < t:
#                 cur = stack.pop()
#                 ans[cur] = i - cur
#             stack.append(i)

#         return ans

        # n = len(temperatures)
        # ans = []
        # for i, temp in enumerate(temperatures):
        #     j = i+1
        #     while j < n and temperatures[j] <= temp:
        #         j += 1
        #     if j == n:
        #         ans.append(0)
        #     else:
        #         ans.append(j-i)
        # return ans
    
        # s = set(temperatures)
        # ans = []
        # for i, temp in enumerate(temperatures):
        #     s.remove(temp)
        #     for j, t in range(temp+1, 101):
        #         if t in s:
            