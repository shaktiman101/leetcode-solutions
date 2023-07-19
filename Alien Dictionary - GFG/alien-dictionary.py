#User function Template for python3
from collections import deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        chr_node_mapping = {chr(97+i):i for i in range(K)}
        node_chr_mapping = {node:ch for ch, node in chr_node_mapping.items()}
        
        edges = []
        for i in range(1,N):
            word1, word2 = alien_dict[i-1], alien_dict[i]
            for ch1, ch2 in zip(word1, word2):
                if ch1 != ch2:
                    edges.append((ch1, ch2))
                    flag = 1
                    break
            # if flag == 0:
            #     edges.append(word2[len(word1)])
        # print(edges)
        
        adj = [[] for _ in range(K)]
        for u, v in edges:
            u = chr_node_mapping[u]
            v = chr_node_mapping[v]
            adj[u].append(v)
        
        in_degree = [0]*K
        for node in range(K):
            for adj_node in adj[node]:
                in_degree[adj_node] += 1
                
        queue = deque([])
        for node, deg in enumerate(in_degree):
            if deg == 0:
                queue.append(node)
              
        # print(queue)
        # return []
        
        dict_order = []  
        while queue:
            node = queue.popleft()
            ch = node_chr_mapping[node]
            dict_order.append(ch)
            
            for adj_node in adj[node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    queue.append(adj_node)
            
        return dict_order



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends