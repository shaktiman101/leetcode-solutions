class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1-x2 == 0:
                return inf
            return (y1-y2)/(x1-x2)
        
        ans = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for j, p2 in enumerate(points[i+1:]):
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans+1
    
        n = len(points)
        if n == 1:
            return 1
        x2, y2 = points[1]
        x1, y1 = points[0]
        x, y = x2-x1, y2-y1
        if y == 0:
            slope = f"{x}/{y}"
        else:
            slope = x/y
        max_count = 2
        hashmap = {slope: set(((x1, y1), (x2, y2)))}
        
        for i in range(2, n):
            x2, y2 = points[i]
            j = i-1
            while j >= 0:
                x1, y1 = points[j]
                x, y = x2-x1, y2-y1
                if y == 0:
                    slope = f"{1}/{y}"
                else:
                    slope = x/y
                if slope in hashmap:
                    hashmap[slope].add((x2, y2))
                else:
                    hashmap[slope] = set(((x1, y1), (x2, y2)))
                if len(hashmap[slope]) > max_count:
                    max_count = len(hashmap[slope])
                j -= 1
        print(hashmap)
        return max_count
    
    
        
            # x2, y2 = points[i]
            # slope = f"{x2-x1}/{y2-y1}"
            # if slope in hashmap:
            #     hashmap[slope] += 1
            #     if hashmap[slope] > max_count:
            #         max_count = hashmap[slope]
            # else:
            
        