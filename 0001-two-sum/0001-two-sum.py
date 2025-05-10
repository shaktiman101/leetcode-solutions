class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for idx, num in enumerate(nums):
            if target-num in pair:
                return idx, pair[target-num]
            pair[num] = idx 
