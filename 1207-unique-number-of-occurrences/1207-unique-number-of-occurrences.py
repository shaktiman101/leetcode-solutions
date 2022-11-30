from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_count = Counter(arr)
        freq_set = set()
        for freq in arr_count.values():
            if freq in freq_set:
                return False
            freq_set.add(freq)
        return True
        
        