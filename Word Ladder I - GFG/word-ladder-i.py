from collections import deque
class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
	    unique_wordList = set(wordList)
	    
	    if not targetWord in unique_wordList:
	        return 0
	    if not startWord in unique_wordList:
	        wordList.append(startWord)
	        
	    
		n = len(wordList)
		adj = [[] for _ in range(n)]
		word_node_mapping, node_word_mapping = {}, {}
		word_node_mapping[startWord] = 0
		node_word_mapping[0] = startWord
		
		node_idx = 1
		for word in wordList:
		    if word == startWord:
		        continue
		    word_node_mapping[word] = node_idx
		    node_word_mapping[node_idx] = word
		    node_idx += 1
		  
# 		print(word_node_mapping)
# 		print(word_node_mapping[0])
# 		return 1
		for i in range(n):
		    for j in range(i+1, n):
		        word1, word2 = wordList[i], wordList[j]
		        
		        count = 0
    		    for ch1, ch2 in zip(word1, word2):
    		        if ch1 != ch2:
    		            count += 1
    		    if count == 1:
    		        adj[word_node_mapping[word1]].append(word_node_mapping[word2])
    		        adj[word_node_mapping[word2]].append(word_node_mapping[word1])
    		        
        queue = deque([(0, 0)])
        shortest_dist = [float('inf')]*n
        shortest_dist[0] = 0
        while queue:
            node, dist = queue.popleft()
            for adj_node in adj[node]:
                if dist+1 < shortest_dist[adj_node]:
                    shortest_dist[adj_node] = dist+1
                    queue.append((adj_node, dist+1))
            
        target = word_node_mapping[targetWord]        
        if shortest_dist[target] == float('inf'):
            return 0
        return shortest_dist[target]+1
            


#{ 
 # Driver Code Starts
# from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends