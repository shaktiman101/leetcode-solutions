class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashmap = {}
        # n = len(nums)
        # for i in range(n):
        #     h = hashmap.get(nums[i], -1)
        #     if h != -1 and abs(h-i) <= k:
        #         return True
        #     hashmap[nums[i]] = i
        # return False
    
        hashmap = {}
        for i, num in enumerate(nums):
            idx = hashmap.get(num, -1) #.append(i)
            if idx != -1 and abs(idx-i) <= k:
                return True
            hashmap[num] = i
            
        # print(hashmap)
        return False