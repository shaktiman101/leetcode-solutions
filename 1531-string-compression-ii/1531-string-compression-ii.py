class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def counter(start, last, last_count, left): #count the cost of compressing from the start
            if left < 0:
                return float('inf') # this is impossible
            if start >= len(s):
                return 0
            if s[start] == last:
				# we have a stretch of the last_count of the same chars, what is the cost of adding one more? 
                incr = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
				# no need to delete here, if we have a stretch of chars like 'aaaaa' - we delete it from the beginning in the else delete section
                return incr + counter(start+1, last, last_count+1, left) # we keep this char for compression
            else:
                keep_counter = 1 + counter(start+1, s[start], 1, left)
				# delete this char
                del_counter =  counter(start + 1, last, last_count, left - 1)
                return min(keep_counter, del_counter)
            
        return counter(0, "", 0, k)
    
#         n, count = len(s), 1
#         compressed = s[0] #""
        
#         for i in range(1, n):
#             if s[i] == s[i-1]:
#                 count += 1
#             else:
#                 if count > 1:
#                     compressed += str(count)
#                 compressed += s[i]
#                 count = 1
#         if count > 1:
#             compressed += str(count)
        
#         return len(compressed)