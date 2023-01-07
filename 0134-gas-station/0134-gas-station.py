class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start
    
        
        diff = []
        n = len(gas)
        for g, c in zip(gas, cost):
            diff.append(g-c)
        if sum(diff) < 0:
            return -1
        
        residual = diff[0]
        start = 0
        for i in range(n):
            if diff[i]+residual > residual:
                start = i
                
            residual += diff[i]
        return start
            