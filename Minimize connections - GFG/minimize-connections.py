from typing import List


class Solution:
    def minimumConnections(self, n : int, m : int, c : List[List[int]]) -> int:
        connections = c
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]
        
        def find_uparent(node):
            if node == parent[node]:
                return node
            parent[node] = find_uparent(parent[node])
            return parent[node]
        
        def union(u, v):
            pu = find_uparent(u)
            pv = find_uparent(v)
            if pu == pv:
                return 1
            
            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]
            return 0
        
        extra_conn = 0    
        for u, v in connections:
            extra_conn += union(u, v)
            
        total_comp = 0
        for node in range(n):
            if node == parent[node]:
                total_comp += 1
        
        connection_needed = total_comp-1
        if connection_needed <= extra_conn:
            return connection_needed
        return -1
        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        
        c=IntMatrix().Input(m, m)
        
        obj = Solution()
        res = obj.minimumConnections(n, m, c)
        
        print(res)
        

# } Driver Code Ends