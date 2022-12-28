import heapq
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # piles = sorted(piles, reverse=True)
        piles = list(map(lambda x: -x, piles))
        heapq.heapify(piles)
        
        while k:
            largest = heapq.heappop(piles)*-1
            heapq.heappush(piles, math.ceil(largest/2)*-1)
            k -= 1
        return abs(sum(piles))