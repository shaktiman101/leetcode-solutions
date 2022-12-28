import heapq
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = list(map(lambda x: -x, piles))
        heapq.heapify(piles)
        
        while k:
            # largest = heapq.heappop(piles)*-1
            # heapq.heappush(piles, math.ceil(largest/2)*-1)
            heapq.heapreplace(piles, piles[0]//2)
            k -= 1
        return abs(sum(piles))