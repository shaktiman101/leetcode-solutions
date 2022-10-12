class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        n = len(nums)
        for i in range(2, n):
            if nums[i]+nums[i-1] > nums[i-2]:
                return nums[i]+nums[i-1]+nums[i-2]
        return 0