class Solution:
    def climbStairs(self, n: int) -> int:
#         n1, n2 = 1, 2
#         if n < 2:
#             return n1
        
#         for i in range(3, n+1):
#             tmp = n2
#             n2 = n1+n2
#             n1 = tmp
#         return n2
        mem = {}
        def solve(n):
            if n <= 2:
                return n
            if mem.get(n, None):
                return mem.get(n)
            n1 = solve(n-1)
            mem[n-1] = n1
            n2 = solve(n-2)
            mem[n-2] = n2
            return n1 + n2
        
        return solve(n)