class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
            
        count = 0
        for col in range(n):
            prev_word = strs[0]
            for curr_word in strs[1:]:
                if prev_word[col] > curr_word[col]:
                    count += 1
                    break
                prev_word = curr_word
        return count
            
            
        