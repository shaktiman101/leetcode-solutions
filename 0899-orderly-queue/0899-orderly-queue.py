class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return "".join(sorted(s)) if k > 1 else min(s[i:] + s[:i] for i in range(len(s)))
        n = len(s)
        s = list(s)
        for i in range(k+1):
            for j in range(i,n):
                if s[i] > s[j]:
                    s[i], s[j] = s[j], s[i]
        return ''.join(s)
    
        # for i in range(len(S)):
        #     sorted(S) if K > 1 else min(S[i:] + S[:i] 
            
        