class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target-num in hashmap:
                return (hashmap[target-num], i)
            hashmap[num] = i
        
        hashmap = {}
        for i, num in enumerate(nums):
            if target-num in hashmap:
                return [i, hashmap[target-num]]
            else:
                hashmap[num] = i
        
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            hashmap[target-nums[i]] = i
            
        