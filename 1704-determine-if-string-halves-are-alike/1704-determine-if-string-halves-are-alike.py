class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = set(list("aeiouAEIOU"))
        count = 0
        for i in range(n//2):
            if s[i] in vowels:
                count += 1
        for i in range(n//2,n):
            if count < 0:
                return False
            if s[i] in vowels:
                count -= 1
        if count == 0:
            return True
        return False