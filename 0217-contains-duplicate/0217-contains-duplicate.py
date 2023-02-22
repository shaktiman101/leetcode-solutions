class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set(nums)
        return len(unique_nums)!=len(nums)
        
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
        