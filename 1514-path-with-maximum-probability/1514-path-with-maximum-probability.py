import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]
        for i, src_dst in enumerate(edges):
            src, dst = src_dst
            adj[src].append((succProb[i], dst))
            adj[dst].append((succProb[i], src))
            
        heap = [(-1, start)]
        heapq.heapify(heap)
        prob = [0]*n
        prob[start] = 1
        
        while heap:
            curr_prob, curr_node = heapq.heappop(heap)
            curr_prob *= -1
            for adj_prob, adj_node in adj[curr_node]:
                tmp_prob = curr_prob * adj_prob
                if tmp_prob > prob[adj_node]:
                    prob[adj_node] = tmp_prob
                    heapq.heappush(heap, (-tmp_prob, adj_node))
        # print(prob)
        return prob[end]