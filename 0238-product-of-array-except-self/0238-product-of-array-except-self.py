from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_freq = Counter(nums)
        if num_freq.get(0, 0) > 1:
            return [0]*len(nums)
    
        prod = 1
        for num in nums:
            if num == 0:
                continue
            prod *= num

        result = []
        for i, num in enumerate(nums):
            if num == 0:
                result = [0]*len(nums)
                result[i] = prod
                return result
            else:
                result.append(prod//num)    
        return result