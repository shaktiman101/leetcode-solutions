#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        # heap = [(0, 0)]
        # heapq.heapify(heap)
        
        # def is_cycle(node):
        #     pass
        
        # span_weight = 0
        # while heap:
        #     weight, node = heapq.heappop(heap)
        #     if not is_cycle(node):
        #         span_weight += weight
        #         for adj_node, adj_weight in adj[node]:
        #             heapq.heappush(heap, (adj_weight, adj_node))
        # return span_weight
        
        # adj_list = [[] for _ in range(V)]
        # for u, v, w in adj:
        #     adj_list[u].append((v, w))
        #     adj_list[v].append((u, w))
            
        heap = []
        heapq.heapify(heap)
        # heapq.heappush(heap, (0, 0, -1))    # edge_weight, curr_node, parent_node
        heapq.heappush(heap, (0, 0))
        
        visited = [False]*V
        mst_edges = []
        mst_weight, edge_count = 0, 0
        
        while heap: # and edge_count < V-1:
            # weight, curr_node, parent_node = heapq.heappop(heap)
            weight, curr_node = heapq.heappop(heap)
            if visited[curr_node]:
                continue
            # if parent_node != -1 and not visited[curr_node]:
                # mst_edges.append((parent_node, curr_node))
                # edge_count += 1
                
            visited[curr_node] = True
            mst_weight += weight
                
                
            
            for adj_node, adj_weight in adj[curr_node]:
                if not visited[adj_node]:
                    heapq.heappush(heap, (adj_weight, adj_node))
                    
        return mst_weight


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends