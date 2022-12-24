class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) // 2 # Note this is N/2, ie no. of elements required in each.
        
        def get_sums(nums): # generate all combinations sum of k elements
            ans = {}
            N = len(nums)
            for k in range(1, N+1): # takes k element for nums
                sums = []
                for comb in combinations(nums, k):
                    s = sum(comb)
                    sums.append(s)
                ans[k] = sums
            return ans
        
        left_part, right_part = nums[:N], nums[N:]
        left_sums, right_sums = get_sums(left_part), get_sums(right_part)
        ans = abs(sum(left_part) - sum(right_part)) # the case when taking all N from left_part for left_ans, and vice versa
        total = sum(nums) 
        half = total // 2 # the best sum required for each, we have to find sum nearest to this
        for k in range(1, N):
            left = left_sums[k] # if taking k no. from left_sums
            right = right_sums[N-k] # then we have to take remaining N-k from right_sums.
            right.sort() # sorting, so that we can binary search the required value
            for x in left:
                r = half - x # required, how much we need to add in x to bring it closer to half.
                p = bisect.bisect_left(right, r) # we are finding index of value closest to r, present in right, using binary search
                for q in [p, p-1]:
                    if 0 <= q < len(right):
                        left_ans_sum = x + right[q]
                        right_ans_sum = total - left_ans_sum
                        diff = abs(left_ans_sum - right_ans_sum)
                        ans = min(ans, diff) 
        return ans
        
        
        n = len(nums)
        total = 0
        for num in nums:
            total += abs(num)
        k = total//2
        
        dp = [[False]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1,n+1):
            for j in range(1, k+1):
                take = False
                if j >= nums[i-1]:
                    # print(abs(j-nums[i-1]))
                    take = dp[i-1][j-abs(nums[i-1])]
                dp[i][j] = take or dp[i-1][j]
        # return dp[n][k]
        print(dp[n])
        for i in range(k, -1, -1):
            if dp[n][i]:
                return abs(i - (total - i))

        