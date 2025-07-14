class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # zero_idx = []
        # for idx, num in enumerate(nums):
        #     if num == 0:
        #         zero_idx.append(idx)
        n = len(nums)
        if n == 1:
            return True

        max_idx_reachable = 0
        for idx, num in enumerate(nums):
            if idx >= max_idx_reachable and num==0:
                return False
            max_idx_reachable = max(max_idx_reachable, idx+num)
            if max_idx_reachable >= n-1:
                return True
        return True

        