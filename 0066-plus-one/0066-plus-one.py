class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 1
        for digit in digits[::-1]:
            tmp = digit+carry
            carry = tmp//10
            ans.append(tmp%10)
            # print(tmp, tmp//10)
        if carry:
            ans.append(carry)
        return ans[::-1]