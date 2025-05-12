from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        result = sorted(num_freq.items(), key=lambda x: x[1], reverse=True)[:k]
        return [pair[0] for pair in result]