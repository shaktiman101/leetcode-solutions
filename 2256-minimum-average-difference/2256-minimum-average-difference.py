class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        first_half = 0
        min_diff = float('inf')
        ans = 0
        for i in range(n):
            first_half += nums[i]
            second_half = total_sum - first_half
            # print(first_half, second_half)
            first_half_avg = int((first_half)/(i+1))
            # if first_half_avg%1 == 0.5:
            #     first_half_avg = int(first_half_avg)
            
            second_half_avg = 0
            if i < n-1:
                second_half_avg = int((second_half)/(n-i-1))
            #     if second_half_avg%1 == 0.5:
            #         second_half_avg = int(second_half_avg)
            # print(first_half_avg, second_half_avg)
            abs_diff = abs(first_half_avg - second_half_avg)
            # print(round(first_half_avg), round(second_half_avg))
            if abs_diff < min_diff:
                min_diff = abs_diff
                ans = i
        return ans