class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_water = 0
        left, right = 0, n-1

        while left < right:
            if height[left] < height[right]:
                water = (right-left) * height[left]
                left += 1
            else:
                water = (right-left) * height[right]
                right -= 1
            max_water = max(water, max_water)
        return max_water