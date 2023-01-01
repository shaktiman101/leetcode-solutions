class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = len(pattern)
        words = s.split()
        n = len(words)
        if m != n:
            return False
        
        hashmap, rev_hashmap = {}, {}
        for ch, word in zip(pattern, words):
            if not (ch in hashmap or word in rev_hashmap):
                hashmap[ch] = word
                rev_hashmap[word] = ch
            else:
                word2 = hashmap.get(ch, None)
                if word2 and word != word2:
                    return False
                ch2 = rev_hashmap.get(word, None)
                if ch2 and ch != ch2:
                    return False
        return True
                
        