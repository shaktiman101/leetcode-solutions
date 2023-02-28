class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        start, end = 0, len(numbers)-1
        
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            if target - numbers[end] < numbers[start]:
                end -= 1
            else:
                start += 1
                
            
        