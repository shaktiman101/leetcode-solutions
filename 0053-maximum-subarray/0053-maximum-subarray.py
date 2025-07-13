class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]

        for num in nums[1:]:
            if cur_sum < 0:
                cur_sum = num
            else:
                cur_sum += num
            max_sum = max(max_sum, cur_sum)
        return max(max_sum, cur_sum)