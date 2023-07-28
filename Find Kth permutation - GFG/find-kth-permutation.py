#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
from typing import List
# import math

class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        def factorial(n):
            if n <= 1:
                return 1
            return n*factorial(n-1)
        
        nums = []
        for i in range(1,n+1):
            nums.append(str(i))
        nums = ''.join(nums)
        
        # total_perm = fact(n)
        # total_perm_n1 = fact(n-1)
        
        # factor = 1
        # while total_perm_n1<k:
        #     k -= total_perm_n1
        #     factor += 1
        
        # nums = []
        # for i in range(1, n+1):
        #     if i == factor:
        #         continue
        #     nums.append(str(i))
            
        # res = []
        # visited = [False]*n
        
        
        # def permutation(tmp):
        #     if len(tmp) == len(nums):
        #         res.append(''.join(tmp))
        #         return
            
        #     for i in range(len(nums)):
        #         if visited[i]:
        #             continue
                
        #         visited[i] = True
        #         tmp.append(nums[i])
        #         permutation(tmp)
        #         visited[i] = False
        #         tmp.pop()
            
            
        # permutation([])
        # return str(factor)+res[k-1]
        k = k-1
        res = []
        
        def func(n, k, nums):
            if n < 0:
                return
            
            fact = factorial(n)
            idx = k//fact
            res.append(nums[idx])
            func(n-1, k%fact, nums[:idx]+nums[idx+1:])
            
        func(n-1, k, nums)
        return ''.join(res)
            
        
        
        


#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N, K = map(int, input().split())
        
        obj = Solution()
        res = obj.kthPermutation(N, K)
        
        print(res)
        

# } Driver Code Ends