class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        i = 0
        while i < n-1: 
            if s[i].islower() and s[i+1].isupper() and s[i] == s[i+1].lower():
                s = s[:i]+s[i+2:]
                n = len(s)
                i -= 2
            elif s[i].isupper() and s[i+1].islower() and s[i].lower() == s[i+1]:
                s = s[:i]+s[i+2:]
                n = len(s)
                i -= 2
            i += 1
            i = max(0, i)
        return s
                
                
        