class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        
        def merge(arr, low, mid, high):
            inv_count = 0
            arr_new = []
            i, j = low, mid+1
            
            while i <= mid and j <= high:
                if arr[i] <= arr[j]:
                    arr_new.append(arr[i])
                    i += 1
                else:
                    arr_new.append(arr[j])
                    j += 1
                    inv_count += (mid-i+1)
                    
        
            # if i > mid:
            while j <= high:
                arr_new.append(arr[j])
                j += 1
        
            # if j > high:
            while i <= mid:
                arr_new.append(arr[i])
                i += 1
                
            # j = 0
            for i in range(low, high+1):
                arr[i] = arr_new[i-low]
                # j += 1
                
            return inv_count
        
            
        def merge_sort(arr, l, r):
            inv_count = 0
            
            if l >= r:
                return inv_count
            
            mid = (l+r)//2
            inv_count += merge_sort(arr, l, mid)
            inv_count += merge_sort(arr, mid+1, r)
            inv_count += merge(arr, l, mid, r)
            return inv_count
                    
        
        return merge_sort(arr, 0, n-1)
        # return inv_count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends