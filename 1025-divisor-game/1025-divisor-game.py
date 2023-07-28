class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False
        if n == 2:
            return True
        
        def get_divisor(n):
            divisor = [1]
            for i in range(2, n//2):
                if n%i == 0:
                    divisor.append(i)
                    if i != n//i:
                        divisor.append(i)
            return divisor
            
        # 1-Alice, 0-Bob
        def func(n, player):
            if n == 1:
                if player:
                    return False
                return True
            
            for div in get_divisor(n):
                return func(n-div, 1-player)
        
        return func(n, 1)
            
            