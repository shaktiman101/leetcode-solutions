from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter(bin(n)).get('1',0)