class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        
        # recursive
#         def func(idx1, idx2):
#             if idx1 >= m or idx2 >= n:
#                 return 0
            
#             if idx1 == m-1 and idx2 == n-1:
#                 if text1[idx1] == text2[idx2]:
#                     return 1
#                 return 0
            
#             c1, c2 = 0, 0
#             if text1[idx1] == text2[idx2]:
#                 c1 = 1 + func(idx1+1, idx2+1)
#             else:
#                 c2 = max(func(idx1+1, idx2),func(idx1, idx2+1))
            
#             return max(c1, c2)
            
#         return func(0, 0)


        # memoized
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def func(idx1, idx2):
            if idx1 < 1 or idx2 < 1:
                return 0
            
            if idx1 == 1 and idx2 == 1:
                if text1[idx1-1] == text2[idx2-1]:
                    return 1
                return 0
            
            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]
            
            c1, c2 = 0, 0
            if text1[idx1-1] == text2[idx2-1]:
                c1 = 1 + func(idx1-1, idx2-1)
            else:
                c2 = max(func(idx1-1, idx2),func(idx1, idx2-1))
            
            dp[idx1][idx2] = max(c1, c2)
            return dp[idx1][idx2]
            
        return func(m, n)
    
    
        # tabulation
        dp = [[0]*(n+1) for _ in range(m+1)]
        # for i in range(m+1):


        for i in range(1, m+1):
            for j in range(1, n+1):

                c1, c2 = 0, 0
                if text1[i] == text2[j]:
                    c1 = 1 + dp[i-1][j-1]
                else:
                    c2 = max(dp[i-1][j], dp[i][j-1])

                dp[i][j] = max(c1, c2)

        return dp[m][n]
            