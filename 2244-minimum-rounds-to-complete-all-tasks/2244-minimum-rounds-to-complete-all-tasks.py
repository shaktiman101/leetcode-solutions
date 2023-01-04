from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_freq = Counter(tasks)
        dp = [-1]*int(1e5+1)
        rounds = 0
        def func(v):
            if v < 2:
                return float('inf')
            if v==2 or v==3:
                return 1
            if dp[v] != -1:
                return dp[v]
            r1 = 1+func(v-3)
            r2 = 1+func(v-2)
            dp[v] = min(r1, r2)
            return dp[v]
        
        for v in task_freq.values():
            if dp[v] != -1:
                rounds += dp[v]
            else:
                tmp = func(v)
                if tmp == float('inf'):
                    return -1
                dp[v] = tmp
                rounds += tmp
        return rounds
    
    
        task_freq = Counter(tasks)
        rounds = 0
        def func(v):
            if v < 2:
                return float('inf')
            if v==2 or v==3:
                return 1
            r1 = 1+func(v-3)
            r2 = 1+func(v-2)
            return min(r1, r2)
        
        for k, v in task_freq.items():
            tmp = func(v)
            if tmp == float('inf'):
                return -1
            rounds += tmp
        return rounds
                
        
            