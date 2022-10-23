class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = sum(nums)
        orig_sum = (n*(n+1))//2
        res = []
        
        # nums = sorted(nums)
        # for i in range(n-1):
        #     if nums[i] == nums[i+1]:
        #         res.append(nums[i])
        #         break
        # res.append(orig_sum+res[0]-actual_sum)
        # return res
    
        nums2 = set(nums)
        set_sum = sum(nums2)
        res.append(actual_sum-set_sum)
        res.append(orig_sum-set_sum)
        return res
        
            