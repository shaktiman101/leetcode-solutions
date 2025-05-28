import heapq
from collections import defaultdict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if n<x:
            return sum(nums)
            
        left, right = 0, 0
        num_count = defaultdict(int)
        result = []

        while right < n:
            if right-left+1 < k:
                num_count[nums[right]] += 1
            else:
                num_count[nums[right]] += 1
                sorted_num = sorted(num_count.items(), key=lambda x: (x[1],x[0]), reverse=True)[:x]
                print(sorted_num)
                sum_ = sum([num*freq for num, freq in sorted_num])
                result.append(sum_)
                num_count[nums[left]] -= 1
                left += 1
            right += 1
        return result