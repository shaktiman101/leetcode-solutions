class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left, right = i+1, n-1
            while left<n and right>i and left < right:
                tmp = nums[left]+nums[right]
                if tmp == target:
                    
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif tmp < target:
                    left += 1
                else:
                    right -= 1
        return list(set(res))