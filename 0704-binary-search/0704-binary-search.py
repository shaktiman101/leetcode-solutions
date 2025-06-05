class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def func(l, r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    return func(mid+1, r)
                else:
                    return func(l, mid-1)
            return -1

        return func(0, len(nums)-1)