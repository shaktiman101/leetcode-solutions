class Solution:
    def removeDuplicates(self, s: str) -> str:
        n, i = len(s), 1
        
        while i < n:
            if s[i] == s[i-1]:
                s = s[:i-1]+s[i+1:]
                n = len(s)
                i -= 1
                i = max(1, i)
            else:
                i += 1
        return s