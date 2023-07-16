#User function Template for python3
from collections import deque
class Solution:
    def findOrder(self, N, m, prerequisites):
        adj = [[] for _ in range(N)]
        
        for u, v in prerequisites:
            adj[v].append(u)

        in_degress = [0]*N
        for node in range(N):
            for adj_node in adj[node]:
                in_degress[adj_node] += 1
                
        queue = deque([])
        for node, deg in enumerate(in_degress):
            if deg == 0:
                queue.append(node)
                
        task_order = []
        while queue:
            node = queue.popleft()
            task_order.append(node)
            
            for adj_node in adj[node]:
                in_degress[adj_node] -= 1
                if in_degress[adj_node] == 0:
                    queue.append(adj_node)
                    
        if len(task_order) != N:
            return []
        return task_order


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends