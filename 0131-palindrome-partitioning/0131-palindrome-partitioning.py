class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        
        def is_palindrome(s_temp):
            if len(s_temp) == 0:
                return False
            
            i, j = 0, len(s_temp)-1
            
            while i<=j:
                if s_temp[i] != s_temp[j]:
                    return False
                i += 1
                j -= 1
            
            return True
        
            
        def backtrack(idx, tmp, s):
            if len(s) == 0:
                res.append(tmp.copy())
                return
            
            for i in range(1, len(s)+1):
                sub1, sub2 = s[:i], s[i:]
                if is_palindrome(sub1):
                    tmp.append(sub1)
                    backtrack(i+1, tmp, sub2)
                    tmp.pop()
                    
        backtrack(0, [], s)
        return res