class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        first = second = float('inf')
        third = 0
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                # third = num
                return True
        return False
        
        # if first < second < third:
        #     return True
        # return False