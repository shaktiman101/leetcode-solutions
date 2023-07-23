#User function Template for python3

class Solution:
    def printUniqueSubset(self, nums):
        nums = sorted(nums)
        n = len(nums)
        res = []
        
        def func(idx, subset):
            if idx >= n:
                res.append(subset.copy())
                return
        
            subset.append(nums[idx])
            func(idx+1, subset)
            subset.pop()
            
            while idx<n-1 and nums[idx]==nums[idx+1]:
                idx += 1
            func(idx+1, subset)
        
        func(0, [])
        return sorted(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        res = ob.printUniqueSubset(nums)
        print('[ ', end = '')
        for subset in res:
            print('[ ', end = '')
            for val in subset:
                print(val, end = ' ')
            print(']', end = '')
        print(' ]')
# } Driver Code Ends