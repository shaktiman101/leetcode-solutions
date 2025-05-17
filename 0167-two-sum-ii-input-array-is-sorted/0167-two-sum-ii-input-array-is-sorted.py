class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        n = len(numbers)

        while left<n and right >= 0 and left < right:
            sum_ = numbers[left]+numbers[right]
            if sum_ == target:
                return [left+1, right+1]
            elif sum_ < target:
                left += 1
            else:
                right -= 1