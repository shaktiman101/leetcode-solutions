#User function Template for python3

from typing import List
from collections import deque

class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # heap = []
        # heapq.heapify(heap)
        # heapq.heappush(heap, (start, 0))
        if start == end:
            return 0
        queue = deque([(start, 0)])
        mod = int(1e5)
        dist = [float('inf')]*mod
        dist[start] = 0
        
        while queue:
            num, steps = queue.popleft()
            
            for multiplier in arr:
                res = num*multiplier%mod
                if steps+1 < dist[res]:
                    dist[res] = steps+1
                    if res == end:
                        return steps+1
                    queue.append((res, steps+1))
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends