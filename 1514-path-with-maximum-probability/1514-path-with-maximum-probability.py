import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = [[] for _ in range(n)]
        for i, edge in enumerate(edges):
            adj_list[edge[0]].append((succProb[i], edge[1]))
            adj_list[edge[1]].append((succProb[i], edge[0]))
            
        max_prob = [float('-inf') for _ in range(n)]
        
        prob_heap = []
        heapq.heapify(prob_heap)
        heapq.heappush(prob_heap, (-1, start_node))
        
        while prob_heap:
            prob, node = heapq.heappop(prob_heap)
            prob *= -1
            
            if prob > max_prob[node]:
                max_prob[node] = prob
                
            for adj_prob, adj_node in adj_list[node]:
                if prob*adj_prob > max_prob[adj_node]:
                    heapq.heappush(prob_heap, (-prob*adj_prob, adj_node))
                    
        if max_prob[end_node] == float('-inf'):
            return 0.0
        return max_prob[end_node]
                
            
        