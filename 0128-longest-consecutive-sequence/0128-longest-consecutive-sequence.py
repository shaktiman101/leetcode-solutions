class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in nums:
            if num-1 not in num_set:
                n = num
                count = 0
                while n in num_set:
                    count += 1
                    n += 1
                res = max(count, res)
        return res