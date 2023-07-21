#User function Template for python3

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        unique_wordList = set(wordList)     # TC: O(n), SC: O(n)
	    
	    if not targetWord in unique_wordList:
	        return 0
	    if not startWord in unique_wordList:
	        wordList.append(startWord)
	        
	    
		n = len(wordList)
		adj = [[] for _ in range(n)]                    # TC: O(n), SC:O(n)
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
		  
		for i in range(n):                          #TC: O(N2*M)
		    for j in range(i+1, n):
		        word1, word2 = wordList[i], wordList[j]
		        
		        count = 0
    		    for ch1, ch2 in zip(word1, word2):
    		        if ch1 != ch2:
    		            count += 1
    		    if count == 1:
    		        adj[word_node_mapping[word1]].append(word_node_mapping[word2])
    		        adj[word_node_mapping[word2]].append(word_node_mapping[word1])
    	
        queue = deque([(0, 0, [startWord])])                         # SC: O(n)
        shortest_dist = [float('inf')]*n                # SC: O(n)
        shortest_dist[0] = 0
        target = word_node_mapping[targetWord]
        parent = [[] for i in range(n)]
        res = []
        
        while queue:                                    # TC: O(N + 2N^2)
            node, dist, path = queue.popleft()
            if node == target:
                res.append(path.copy())
                
            for adj_node in adj[node]:
                adj_node_path = path.copy()
                if dist+1 <= shortest_dist[adj_node]:
                    # parent[node].append(adj_node)
                    adj_node_path.append(node_word_mapping[adj_node])
                    shortest_dist[adj_node] = dist+1
                    queue.append((adj_node, dist+1, adj_node_path))
                
        if shortest_dist[target] == float('inf'):
            return []
        # print(res)
        
        return res
        
        res = []
        def dfs(node, tmp):
            if node == target:
                res.append(tmp.copy())
                return
            
            for adj_node in parent[node]:
                tmp.append(node_word_mapping[adj_node])
                dfs(adj_node, tmp)
                tmp.pop()
            
        dfs(0, [startWord])
        return res #shortest_dist[target]+1


#{ 
 # Driver Code Starts
from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

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
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends