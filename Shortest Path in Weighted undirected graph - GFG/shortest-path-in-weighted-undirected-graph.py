#User function Template for python3
import heapq
class Solution:
    def shortestPath(self, n, m, edges):
        adj_list = [[] for _ in range(n+1)]
        for u, v, w in edges:
            adj_list[u].append((w, v))
            adj_list[v].append((w, u))
            
        min_weight = [float('inf')]*(n+1)
        min_weight[1] = 0
        min_weight_path = [i for i in range(n+1)]
        
        weight_heap = []
        heapq.heapify(weight_heap)
        parent = None
        heapq.heappush(weight_heap, (0, 1))
        
        while weight_heap:
            weight, node = heapq.heappop(weight_heap)
            min_weight_path.append(node)
            
            for adj_weight, adj_node in adj_list[node]:
                if weight+adj_weight < min_weight[adj_node]:
                    min_weight[adj_node] = weight+adj_weight
                    min_weight_path[adj_node] = node
                    heapq.heappush(weight_heap, (weight+adj_weight, adj_node))
                    
        res = [n]
        idx = n
        count = 0
        while res[-1] != 1 and count < n+1:
            res.append(min_weight_path[idx])
            idx = min_weight_path[idx]
            count += 1
        if res[-1] != 1:
            return [-1]
        return res[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends