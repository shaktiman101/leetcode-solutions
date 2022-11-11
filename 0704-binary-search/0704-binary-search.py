class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # def func(st_idx, end_idx):
        #     if st_idx > end_idx:
        #         return -1
        #     mid_idx = (st_idx + end_idx)//2
        #     if target == nums[mid_idx]:
        #         return mid_idx
        #     if target < nums[mid_idx]:
        #         return func(st_idx, mid_idx-1) 
        #     else:
        #         return func(mid_idx+1, end_idx)
        # return func(0, len(nums)-1)            
        
        st_idx, end_idx = 0, len(nums)-1
        while st_idx <= end_idx:
            mid_idx = (st_idx + end_idx)//2
            if target == nums[mid_idx]:
                return mid_idx
            if target < nums[mid_idx]:
                end_idx = mid_idx-1
            else:
                st_idx = mid_idx + 1
        return -1
                
        