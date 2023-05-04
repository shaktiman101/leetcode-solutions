class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        
        k = 0
        for num in nums:
            if num == val:
                k += 1
        # print(k)
        back_idx = n-k
        for i in range(n-k):
            if nums[i] == val:
                while back_idx < n and nums[back_idx] == val:
                    back_idx += 1
                if back_idx == n:
                    break
                nums[i], nums[back_idx] = nums[back_idx], nums[i]
                back_idx += 1
                # print(nums)
        return n-k