class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        # def is_palindrome(st_idx, end_idx):
        #     if st_idx > end_idx:
        #         return True
        #     if s[st_idx] != s[end_idx]:
        #         return False
        #     return is_palindrome(st_idx+1, end_idx-1)

        # recursive
        # def func(st_idx, end_idx, sub):
        #     if st_idx > n-1 or end_idx < 0 or st_idx > end_idx:
        #         return sub
            
        #     if is_palindrome(s, st_idx, end_idx) and end_idx-st_idx+1 > len(sub):
        #         sub = s[st_idx:end_idx+1]
        #         return func(st_idx+1, end_idx-1, sub)
        #     else:
        #         ans1 = func(st_idx+1, end_idx, sub)
        #         ans2 = func(st_idx, end_idx-1, sub)
        #         return ans1 if len(ans1) > len(ans2) else ans2
            
        # return func(0, n-1, "")

        # memoization
        # dp = [[-1]*(n+1) for _ in range(n+1)]
        # def func(st_idx, end_idx, sub):
        #     if st_idx > n-1 or end_idx < 0 or st_idx > end_idx:
        #         return sub
            
        #     if dp[st_idx][end_idx] != -1:
        #         return dp[st_idx][end_idx]

        #     if is_palindrome(s, st_idx, end_idx) and end_idx-st_idx+1 > len(sub):
        #         sub = s[st_idx:end_idx+1]
        #         dp[st_idx][end_idx] = func(st_idx+1, end_idx-1, sub)
        #         return dp[st_idx][end_idx]
        #     else:
        #         ans1 = func(st_idx+1, end_idx, sub)
        #         ans2 = func(st_idx, end_idx-1, sub)
        #         dp[st_idx][end_idx] = ans1 if len(ans1) > len(ans2) else ans2
        #         return dp[st_idx][end_idx]
            
        # return func(0, n-1, "")


        # tabulation
        # dp = [[""]*(n+1) for _ in range(n+1)]

        # sub = ""
        # for st_idx in range(n):
        #     for end_idx in range(st_idx+1, n):
        #         if is_palindrome(st_idx, end_idx) and end_idx-st_idx+1 > len(sub):
        #             sub = s[st_idx:end_idx+1]
        #             dp[st_idx][end_idx] = sub   #dp[st_idx-1][end_idx-1]
        #         else:
        #             ans1 = dp[st_idx-1][end_idx]
        #             ans2 = dp[st_idx][end_idx-1]
        #             dp[st_idx][end_idx] = ans1 if len(ans1) > len(ans2) else ans2
        
        # return dp[n][n]

        # recursive 
        # s2 = s[::-1]
        # longest_sub = ""

        # def func(idx1, idx2, curr_longest):
        #     nonlocal longest_sub

        #     if idx1 < 0 or idx2 < 0:
        #         return

        #     if s[idx1] == s2[idx2]:
        #         func(idx1-1, idx2-1, curr_longest+s[idx1])
        #     else:
        #         longest_sub = curr_longest if len(curr_longest) > len(longest_sub) else longest_sub
        #         func(idx1-1, idx2, "")
        #         func(idx1, idx2-1, "")


        # func(n-1, n-1, "")
        # return longest_sub


        # s2 = s[::-1]
        # longest_sub = ""
        # dp =[[""]*(n+1) for _ in range(n+1)]

        # for idx1 in range(1,n+1):
        #     for idx2 in range(1,n+1):
        #         if s[idx1-1] == s2[idx2-1]:
        #             dp[idx1][idx2] = dp[idx1-1][idx2-1] + s[idx1-1]
        #             longest_sub = dp[idx1][idx2] if len(dp[idx1][idx2]) > len(longest_sub) else longest_sub
        #         # else:
                    
        #             # dp[idx1][idx2] = dp[idx1-1][idx2]
        #             # dp[idx1][idx2] = dp[idx1][idx2-1]
        # print(dp)
        # return longest_sub

        n = len(s)
        def palindrome_at(st_idx, end_idx):
            palin_st, palin_end = st_idx, st_idx

            while st_idx>=0 and end_idx<n and s[st_idx]==s[end_idx]:
                palin_st, palin_end = st_idx, end_idx

                st_idx -= 1
                end_idx += 1
            return palin_st, palin_end
            
            

        palin_st, palin_end = 0, 0
        for center in range(n):
            # check for odd length substring
            odd = palindrome_at(center, center)
            if odd[1]-odd[0] > palin_end-palin_st:
                palin_st, palin_end = odd

            # check for even length substring
            even = palindrome_at(center, center+1)
            if even[1]-even[0] > palin_end-palin_st:
                palin_st, palin_end = even

        return s[palin_st:palin_end+1]



            