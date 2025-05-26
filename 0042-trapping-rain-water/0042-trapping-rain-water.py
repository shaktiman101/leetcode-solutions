class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n<3:
            return 0
        
        left, right = 0, n-1
        water = 0

        while left < right:
            if height[left] < height[right]:
                cur = left + 1
                while height[cur] < height[left]:
                    water += height[left] - height[cur]
                    cur += 1
                left = cur

            else:
                cur = right -1
                while height[cur] < height[right]:
                    water += height[right] - height[cur]
                    cur -= 1
                right = cur
        return water                