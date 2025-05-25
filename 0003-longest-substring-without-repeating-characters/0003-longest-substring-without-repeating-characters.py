class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)
        hashmap = {}
        max_len = 0

        while right < n:
            if s[right] not in hashmap:
                hashmap[s[right]] = right
            else:
                sub_len = right-left
                max_len = max(max_len, sub_len)
                left = max(left, hashmap[s[right]]+1)
                hashmap[s[right]] = right
            right += 1
        return max(max_len, right-left)