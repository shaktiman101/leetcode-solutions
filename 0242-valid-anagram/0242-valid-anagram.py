from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = Counter(s)
        for ch in t:
            if not ch in char_count:
                return False
            char_count[ch] -= 1
            if char_count[ch] == 0:
                char_count.pop(ch)
        if char_count:
            return False
        return True