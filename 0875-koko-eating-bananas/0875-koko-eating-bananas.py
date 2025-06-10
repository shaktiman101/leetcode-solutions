import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        k_max = max(piles)

        def find_k(k):
            hours_needed = 0
            for banana in piles:
                hours_needed += math.ceil(banana/k)
            # print(f"hours needed={hours_needed}, for k={k}")
            # if hours_needed == h:
            #     return hours_needed
            if hours_needed > h:
                return float('inf')
            else:
                return float('-inf')

        left, right = 1, k_max
        min_k = float('inf')
        while left <= right:
            k = (left+right)//2
            hours_needed = find_k(k)
            # print(k, res)
            if hours_needed == float('inf'):
                left = k+1
            elif hours_needed == float('-inf'):
                right = k-1
                min_k = min(min_k, k)
            # else:
            #     return k
        return min_k