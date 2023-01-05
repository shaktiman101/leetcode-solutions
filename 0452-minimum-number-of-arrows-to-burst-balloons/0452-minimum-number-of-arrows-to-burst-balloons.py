class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        n = len(points)
        arrows = 1
        globalX1, globalX2 = points[0]
        
        for i in range(1, n):
            x1, x2 = points[i]
            if x1 <= globalX2:
                globalX1 = max(globalX1, x1)
                globalX2 = min(globalX2, x2)
            else:
                arrows += 1
                globalX1, globalX2 = x1, x2
        return arrows
        