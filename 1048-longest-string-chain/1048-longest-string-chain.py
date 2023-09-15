class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        if n == 1:
            return 1
        
        words = sorted(words, key=lambda x: len(x))
        
        def is_predecessor(word2, word1):
            n1, n2 = len(word1), len(word2)
            if n1 != n2+1:
                return False
            
            count = 0
            i, j = 0, 0
            while i < n1 and j < n2:
                if word1[i] == word2[j]:
                    count += 1
                    j += 1
                i += 1
                
            if count == n2:
                return True
            return False
        
        
        # recursive 
#         def func(idx, prev_idx):
#             if idx == n:
#                 return 0
            
#             l1 = func(idx+1, prev_idx)
#             if prev_idx == -1 or is_predecessor(words[prev_idx], words[idx]):
#                 l1 = max(l1, 1 + func(idx+1, idx))
#             return l1
            
#         return func(0, -1)

        # memoization
        dp = [[-1]*(n+1) for _ in range(n)]
        def func(idx, prev_idx):
            if idx == n:
                return 0
            if dp[idx][prev_idx+1] != -1:
                return dp[idx][prev_idx+1]
            
            l1 = func(idx+1, prev_idx)
            if prev_idx == -1 or is_predecessor(words[prev_idx], words[idx]):
                l1 = max(l1, 1 + func(idx+1, idx))
            
            dp[idx][prev_idx+1] = l1
            return dp[idx][prev_idx+1]
            
        return func(0, -1)