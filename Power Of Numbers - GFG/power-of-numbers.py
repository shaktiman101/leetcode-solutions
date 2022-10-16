#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        mod = int(1e9)+7
        # return (N**R)%mod
        
        def solve(R):
            if R == 0:
                return 1
            if R == 1:
                return N
            tmp = solve(R//2)
            tmp = tmp**2
            if R%2 != 0:
                tmp = N*tmp
            return tmp%mod
        return solve(R)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends