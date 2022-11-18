class Solution:
    def isUgly(self, n: int) -> bool:
        # if n == 1:
        #     return True
        prime = [2, 3, 5]
        
        while n > 1:
            flag = 0
            for p in prime:
                if n//p == n/p:
                    n //= p
                    flag = 1
                    break
            if flag == 0:
                break
        if n == 1:
            return True
        
        return False
        
        