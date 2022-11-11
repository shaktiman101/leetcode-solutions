class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        n = len(nums)
        
        while j < n:
            while j < n and nums[j] == nums[j-1]:
                j +=1
            if j < n:
                nums[i] = nums[j]
                i += 1
                j += 1
        # print(nums)
        return len(nums[:i])
        