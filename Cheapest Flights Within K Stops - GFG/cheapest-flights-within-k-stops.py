#User function Template for python3
from typing import List
import heapq

class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        adj_list = [[] for _ in range(n)]
        for city_from, city_to, price in flights:
            adj_list[city_from].append((city_to, price))
            
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, 0, src))   # stop, price, city
        
        cheapest_flight = [float('inf')]*n
        cheapest_flight[src] = 0
        # dst_flight_price = []
        
        while heap:
            stop, price, city = heapq.heappop(heap)
                
            for adj_city, adj_price in adj_list[city]:
                if price+adj_price < cheapest_flight[adj_city] and stop <= k:
                    cheapest_flight[adj_city] = price+adj_price
                    heapq.heappush(heap, (stop+1, price+adj_price, adj_city))
        
        if cheapest_flight[dst] == float('inf'):
            return -1
        return cheapest_flight[dst]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        n,edge=map(int,input().split())
        flights=[]
        for _ in range(edge):
            temp=list(map(int,input().split()))
            flights.append(temp[:])
        src=int(input())
        dst=int(input())
        k=int(input())
        obj=Solution()
        res=obj.CheapestFLight(n,flights,src,dst,k)
        print(res)

        
        
# } Driver Code Ends