class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # set solution
        # n = len(sentence)
        # if n < 26:
        #     return False
        # s = set()
        # for ch in sentence:
        #     s.add(ch)
        # return len(s)==26
        
        # bit solution
        chr_present = 0
        for ch in sentence:
            chr_present = chr_present | 1 << ord(ch)-ord('a')
        
        return chr_present == ((1<<26)-1)