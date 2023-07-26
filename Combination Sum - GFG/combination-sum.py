#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,A, B):
        # res = []
        # A = sorted(A, reverse=True)
        # def unique_comb(idx, k, tmp):
        #     if idx < 0 or k > B:
        #         return
        #     if k == B:
        #         res.append(tmp.copy())
        #         return
                
        #     # take
        #     k += A[idx]
        #     tmp.append(A[idx])
        #     unique_comb(idx, k, tmp)
            
        #     # not-take
        #     k -= A[idx]
        #     tmp.pop()
        #     unique_comb(idx-1, k, tmp)
        
        # unique_comb(len(A)-1, 0, [])
        # return tuple(set(res))
        
        n = len(A)
        target = B
        A = sorted(A)
        res = []
        
        def func(idx, tmp, target):
            # if target < 0:
            #     return
            
            if target == 0:
                res.append(tmp.copy())
                return
            
            for i in range(idx, n):
                if A[i] > target:
                    return
                if i > idx and A[i] == A[i-1]:
                    continue
                tmp.append(A[i])
                func(i, tmp, target-A[i])
                tmp.pop()
            # func(idx+1, tmp, target)
        
        func(0, [], target)
        return res
            
            

#{ 
 # Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

# } Driver Code Ends