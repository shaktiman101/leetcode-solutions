#User function Template for python3
from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        shortest_dist = [float('inf')]*n
        shortest_dist[src] = 0
        queue = deque([(src, 0)])
        visited = [False]*n
        
        while queue:
            node, dist = queue.popleft()
            for adj_node in adj[node]:
                if not visited[adj_node] and dist+1 < shortest_dist[adj_node]:
                    shortest_dist[adj_node] = dist+1
                    queue.append((adj_node, dist+1))
                    
        for i in range(n):
            if shortest_dist[i] == float('inf'):
                shortest_dist[i] = -1
                
        return shortest_dist

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends