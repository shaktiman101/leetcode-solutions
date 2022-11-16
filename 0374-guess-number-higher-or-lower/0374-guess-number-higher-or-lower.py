# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        ans = n//2
        res = guess(ans)
        st_num, end_num = 1, n
        
        while res != 0:
            ans = (st_num + end_num)//2
            res = guess(ans)
            if res == -1:
                end_num = ans - 1
            elif res == 1:
                st_num = ans + 1
        
        return ans