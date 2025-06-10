class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        min_ = float('inf')
        while left <= right:
            mid = (left + right) >> 1
            if nums[left] > nums[mid]:
                min_ = min(min_, nums[mid])
                right = mid-1
            elif nums[right] < nums[mid]:
                min_ = min(min_, nums[right])
                left = mid+1
            elif nums[left] <= nums[mid] <= nums[right]:
                min_ = min(min_, nums[left])
                return min_
        return min_