class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = {} #set(words)
        for word in words:
            word_dict[word] = word_dict.get(word, 0)+1
            
        count, flag = 0, 0
        for word in words:
            rev = word[::-1]
            if word == rev:
                f = word_dict[word]
                if f > 1:
                    count += 4
                    word_dict[word] -= 2
                elif f == 1 and flag == 0:
                    count += 2
                    flag = 1
                    word_dict[word] -= 1
            elif word_dict.get(rev) and word_dict.get(word):
                count += 4
                word_dict[rev] -= 1
                word_dict[word] -= 1
                
        return count