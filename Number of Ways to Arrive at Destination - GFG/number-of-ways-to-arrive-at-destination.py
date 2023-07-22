#User function Template for python3

from typing import List
from collections import defaultdict
import sys
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))
        
        mod = int(1e9)+7
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, 0))    # time, start_node
        
        # visited = [False]*n
        time_taken = [float('inf')]*n
        time_taken[0] = 0
        count = 0
        ways = [0]*n
        ways[0] = 1
        while heap:
            node, time = heapq.heappop(heap)
            # visited[node] = True
            
            for adj_node, adj_time in adj[node]:
                tmp_time = time+adj_time
                
                if tmp_time < time_taken[adj_node]:
                    time_taken[adj_node] = tmp_time
                    heapq.heappush(heap, (adj_node, tmp_time))
                    ways[adj_node] = ways[node]%mod
                    
                elif tmp_time == time_taken[adj_node]:
                    ways[adj_node] = (ways[node]+ways[adj_node])%mod
                    
                    
        return ways[n-1]
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        adj=[]
        
        for i in range(m):
            tmp =[]
            x,y,z=map(int,input().split())
            tmp.append(x)
            tmp.append(y)
            tmp.append(z)
            adj.append(tmp)
            
        
        
        
       
        obj = Solution()
        res = obj.countPaths(n, adj)
        
        print(res)
        

# } Driver Code Ends