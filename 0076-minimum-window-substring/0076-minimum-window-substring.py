class Solution:
    def minWindow(self, s: str, t: str) -> str:
#         m, n = len(s), len(t)
#         if m < n:
#             return ""
        
#         hashmap = {}
#         for ch in t:
#             hashmap[ch] = hashmap.get(ch, 0)+1
            
#         i, j, res, res_len = 0, 0, "", float('inf')
#         while i < m:
#             if hashmap.get(s[i], None):
#                 break
#             i += 1
#             j += 1
                
#         count = n
#         while i < m:
#             if i-j < n:
#                 if hashmap.get(s[i], 0) > 0:
#                     hashmap[s[i]] -= 1
#                     count -= 1
#             else:
#                 if count == 0:
#                     if (i-j) < res_len:
#                         res = s[j:i]
#                         res_len = len(res)
#                         count += 1
#                     hashmap[s[j]] += 1
#                     j += 1
#                     while j<m and (hashmap.get(s[j], -1) < 0):
#                         if hashmap.get(s[j], None):
#                             hashmap[s[j]] += 1
#                         j += 1
                
#                 elif hashmap.get(s[i], 0) > 0:
#                     hashmap[s[i]] -= 1
#                     count -= 1
#             i += 1
#         if count == 0 and (i-j) < res_len:
#             res = s[j:i]
#         return res
        
        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):          #index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:                     #match all chars
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                missing += 1                     #we missed this first char, so add missing by 1
                if end == 0 or j-i < end-start:  #update window
                    start, end = i, j
                i += 1                           #update i to start+1 for next window
        return s[start:end]