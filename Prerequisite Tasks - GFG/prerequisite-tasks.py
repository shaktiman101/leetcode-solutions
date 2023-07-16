#User function Template for python3
from collections import deque

class Solution:
    def isPossible(self,N,P,prerequisites):
        adj = [[] for _ in range(N)]
        
        for u, v in prerequisites:
            adj[u].append(v)

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
                    
        return len(task_order)==N

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,P,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends