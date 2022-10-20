class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_count = {}
        for word in words:
            freq_count[word] = freq_count.get(word, 0) + 1
        
        res = [(v, k) for k, v in freq_count.items()]
        res = sorted(res, key=lambda x: x[1])
        res = sorted(res, key=lambda x: x[0], reverse=True)
        return [w[1] for w in res[:k]]
        