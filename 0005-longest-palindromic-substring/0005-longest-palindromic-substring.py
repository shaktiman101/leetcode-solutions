class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[""]*(n+1) for _ in range(n)]

        def is_palindrome(left, right):
            while left<right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def func(left, right):
            if left>=n or right<0 or left>right:
                return ""
            if left == right:
                return s[left]
            if dp[left][right]:
                return dp[left][right]

            # if s[left] == s[right]:
            #     dp[left][right] = s[left]+func(left+1, right-1)+s[left]
            #     return dp[left][right]
            if is_palindrome(left, right):
                dp[left][right] = s[left: right+1]
                return dp[left][right]
            else:
                s1 = func(left+1, right)
                s2 = func(left, right-1)
                dp[left][right] = s1 if len(s1) > len(s2) else s2
                return dp[left][right]

        return func(0, n-1)