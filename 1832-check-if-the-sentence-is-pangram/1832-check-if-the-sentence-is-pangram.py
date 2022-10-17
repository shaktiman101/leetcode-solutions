class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        n = len(sentence)
        if n < 26:
            return False
        s = set()
        for ch in sentence:
            s.add(ch)
        return len(s)==26