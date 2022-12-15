class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #tabulation
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1]==text2[j-1]:
                    ans = 1+dp[i-1][j-1]
                else:
                    ans = max(dp[i-1][j], dp[i][j-1])
                dp[i][j] = ans
        
        return dp[m][n]
        
        # memoization
        m, n = len(text1), len(text2)
        dp = [[0]*n for _ in range(m)]
        def func(m, n):
            if m < 0 or n < 0:
                return 0
            if dp[m][n]:
                return dp[m][n]
            
            if text1[m]==text2[n]:
                ans = 1+func(m-1, n-1)
            else:
                ans = max(func(m-1, n), func(m, n-1))
            dp[m][n] = ans
            return ans
        
        func(m-1, n-1)
        return dp[-1][-1]
    
        
        # recursive
        m, n = len(text1), len(text2)        
        def func(m, n, subseq_len):
            if m < 0 or n < 0:
                return 0
            if text1[m]==text2[n]:
                return 1+func(m-1, n-1, subseq_len+1)
            else:
                return max(func(m-1, n, subseq_len), func(m, n-1, subseq_len))
        
        return func(m-1, n-1, 0)