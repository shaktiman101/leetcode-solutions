class Solution:
    def frequencySort(self, s: str) -> str:
        chr_count = {}
        for ch in s:
            chr_count[ch] = chr_count.get(ch, 0) + 1
        chr_count_li = [(v, k) for k, v in chr_count.items()]
        chr_count_li = sorted(chr_count_li, reverse=True)
        
        res = ""
        for ele in chr_count_li:
            res += ele[1]*ele[0]
        return res
        