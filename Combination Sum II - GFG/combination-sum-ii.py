#User function Template for python3

class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates = sorted(candidates, reverse=True)
        
        def func(idx, target, tmp):
            if idx < 0:
                if target == 0:
                    res.append(tmp.copy())
                return
            
            if candidates[idx] <= target:
                    tmp.append(candidates[idx])
                    func(idx-1, target-candidates[idx], tmp)
                    tmp.pop()
            while idx > 0 and candidates[idx] == candidates[idx-1]:
                idx -= 1
            func(idx-1, target, tmp)
        
        func(len(candidates)-1, target, [])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, target = list(map(int, input().split()))
        candidates = list(map(int, input().split()))
        ob = Solution()
        res = ob.combinationSum2(candidates, target)
        res.sort()
        print('[ ', end = '')
        for subset in res:
            print('[ ', end = '')
            for val in subset:
                print(val, end = ' ')
            print(']', end = '')
        print(' ]')
# } Driver Code Ends