from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = [] #heapq.heapify([])
        self.large = [] #heapq.heapify([])
        
    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
                    

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0])/2
        else:
            return self.large[0]
        
    # def __init__(self):
    #     self.arr = []

#     def addNum(self, num: int) -> None:
#         st_idx, end_idx = 0, len(self.arr)-1
#         # idx_to_insert = 0
#         while st_idx <= end_idx:
#             mid_idx = (st_idx+end_idx)//2
#             if self.arr[mid_idx] == num:
#                 st_idx = mid_idx
#                 break
#             if num < self.arr[mid_idx]:
#                 end_idx = mid_idx - 1
#             else:
#                 st_idx = mid_idx + 1
#         self.arr.insert(st_idx, num)
                    

#     def findMedian(self) -> float:
#         n = len(self.arr)
#         # print(self.arr)
#         if n:
#             if n%2 != 0:
#                 return self.arr[n//2]
#             else:
#                 mid = n//2
#                 return (self.arr[mid]+self.arr[mid-1])/2
#         return 0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()