class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        
        for i, num in enumerate(nums[:-1]):
            target = 0-num
            start, end = i+1, n-1
            while start < end:
                if nums[start]+nums[end] > target:
                    end -= 1
                elif nums[start]+nums[end] < target:
                    start += 1
                else:
                    ans.add((num, nums[start], nums[end]))
                    start += 1
                    end -= 1
        return ans