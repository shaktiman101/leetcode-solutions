class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for ch in s:
            if ans and ans[-1] == ch:
                ans.pop()
            else:
                ans.append(ch)
        return "".join(ans)
    
#         n, i = len(s), 1
        
#         while i < n:
#             if s[i] == s[i-1]:
#                 s = s[:i-1]+s[i+1:]
#                 n = len(s)
#                 i -= 1
#                 i = max(1, i)
#             else:
#                 i += 1
#         return s