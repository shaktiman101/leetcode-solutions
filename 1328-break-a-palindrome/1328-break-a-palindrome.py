class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = ""
        n = len(palindrome)
        if n == 1:
            return ans
        
        flag = 0
        for i in range(n//2):
            if ord(palindrome[i]) > 97:
                ans = palindrome[:i]+'a'+palindrome[i+1:]
                flag = 1
                break
        if flag == 0:
            ans = palindrome[:-1]+'b'
        return ans