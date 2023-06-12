class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        res, tmp = [], [str(nums[0])]
        num = nums[0]
        
        for i in range(1,n):
            if nums[i] != num+1:
                tmp.append("->")
                tmp.append(str(num))
                res.append(''.join(tmp))
                tmp.clear()
                tmp.append(str(nums[i]))
            num = nums[i]
        if tmp:
            if tmp[-1] != num:
                tmp.append('->')
                tmp.append(str(num))
            res.append(''.join(tmp))
        
        for i, ans in enumerate(res):
            num1, num2 = ans.split('->')
            if num1 == num2:
                res[i] = str(num1)
        return res
            
        