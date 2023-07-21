from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         ## this approach won't work on wordList.length > 150
#         startWord, targetWord  = beginWord, endWord
#         unique_wordList = set(wordList)     # TC: O(n), SC: O(n)
	    
#         if not targetWord in unique_wordList:
#             return 0
#         if not startWord in unique_wordList:
#             wordList.append(startWord)
	        
	    
#         n = len(wordList)
#         adj = [[] for _ in range(n)]                    # TC: O(n), SC:O(n)
#         word_node_mapping, node_word_mapping = {}, {}
#         word_node_mapping[startWord] = 0
#         node_word_mapping[0] = startWord

#         node_idx = 1
#         for word in wordList:
#             if word == startWord:
#                 continue
#             word_node_mapping[word] = node_idx
#             node_word_mapping[node_idx] = word
#             node_idx += 1
		  
#         for i in range(n):                          #TC: O(N2*M)
#             for j in range(i+1, n):
#                 word1, word2 = wordList[i], wordList[j]

#                 count = 0
#                 for ch1, ch2 in zip(word1, word2):
#                     if ch1 != ch2:
#                         count += 1
#                 if count == 1:
#                     adj[word_node_mapping[word1]].append(word_node_mapping[word2])
#                     adj[word_node_mapping[word2]].append(word_node_mapping[word1])
    		        
#         queue = deque([(0, 0)])                         # SC: O(n)
#         shortest_dist = [float('inf')]*n                # SC: O(n)
#         shortest_dist[0] = 0
#         while queue:                                    # TC: O(N + 2N^2)
#             node, dist = queue.popleft()
#             for adj_node in adj[node]:
#                 if dist+1 < shortest_dist[adj_node]:
#                     shortest_dist[adj_node] = dist+1
#                     queue.append((adj_node, dist+1))
            
#         target = word_node_mapping[targetWord]        
#         if shortest_dist[target] == float('inf'):
#             return 0
#         return shortest_dist[target]+1

        set_wordList = set(wordList)
        if not endWord in set_wordList:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            word_li = list(word)
            
            for i in range(len(word_li)):
                orig = word_li[i]
                
                for j in range(26):
                    word_li[i] = chr(97+j)
                    changed_word = ''.join(word_li)
                    
                    if changed_word in set_wordList:
                        queue.append((changed_word, dist+1))
                        set_wordList.remove(changed_word)
                word_li[i] = orig
                        
        return 0