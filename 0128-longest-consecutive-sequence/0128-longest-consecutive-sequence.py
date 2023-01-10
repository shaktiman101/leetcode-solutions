class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set([])
        min_num, max_num = float('inf'), float('-inf')
        for num in nums:
            # num_set[num] = num_set.get(num, 0)+1
            num_set.add(num)
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num
        
        ans, count = 0, 0
        # for i in range(min_num, max_num+1):
        #     if i in num_set:
        #         count += 1 #num_set[i]
        #     else:
        #         ans = max(ans, count)
        #         count = 0
        # return max(ans, count)
        ans, count = 1, 1
        for num in nums:
            if num-1 not in num_set:
                tmp = num+1
                while tmp in num_set:
                    count += 1
                    tmp += 1
                else:
                    ans = max(ans, count)
                    count = 1
                
        return max(ans, count)
        
        
        
        
        n = len(nums)
        if n == 0:
            return 0
        
        ele = set()
        smallest, largest = nums[0], nums[0]
        for num in nums:
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num
            ele.add(num)
        
        lcs, lcs_sub = 0, 0
        for num in nums:
            tmp = num
            while tmp in ele:
                lcs_sub += 1
                tmp += 1
            if lcs_sub > lcs:
                lcs = lcs_sub
            lcs_sub = 0
        return lcs
