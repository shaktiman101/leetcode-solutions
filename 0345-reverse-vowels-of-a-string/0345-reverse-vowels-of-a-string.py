class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        rev_vowels = []
        for j in range(len(s)-1, -1, -1):
            if s[j] in vowels:
                rev_vowels.append(s[j])
                
        new_s, i = [], 0
        for ch in s:
            if ch in vowels:
                new_s.append(rev_vowels[i])
                i += 1
            else:
                new_s.append(ch)
        return ''.join(new_s)
        
        # i, j = 0, len(s)-1
        # while i<j:
        #     if s[i] not in vowels:
        #         i += 1
        #     elif s[j] not in vowels:
        #         j -= 1
        #     elif s[i] in vowels and s[j] in vowels:
        #         s[i], s[j] = s[j], s[i]
        #         i += 1
        #         j -= 1
        # return s