class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         if n < 2:
#             return 0
        
#         smallest, largest = n-1, n-1
#         d = {}
#         for i in range(n-2, -1, -1):
#             if prices[i] > prices[largest]:
#                 largest = i
#             if prices[i] < prices[smallest]:
#                 smallest = i
#             if smallest < largest:
#                 d[i] = [smallest, largest]
        
#         smallest, largest = 0, 0
#         for i in range(1, n):
#             if prices[i] > prices[largest]:
#                 largest = i
#             if prices[i] < prices[smallest]:
#                 smallest = i
#             if smallest < largest:
#                 d[i] = [smallest, largest]
            
#         max_profit = 0
#         for _, v in d.items():
#             max_profit = max(max_profit, prices[v[1]]-prices[v[0]])
#         return max_profit

        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit  
    
    
        n = len(prices)
        if n == 1:
            return 0
        
        buy_day, sell_day = 0, 0
        j = n-1
        profit = float('-inf')
        
        buy_idx = [0]
        for i in range(1, n-1):
            if prices[i] < prices[buy_idx[-1]]:
                buy_idx.append(i)
            else:
                buy_idx.append(buy_idx[-1])
        
        sell_idx = [1]
        for i in range(2, n):
            if prices[i] > prices[sell_idx[-1]]:
                sell_idx.append(i)
            else:
                sell_idx.append(sell_idx[-1])
        
        profit = float('-inf')
        for buyi, selli in zip(buy_idx, sell_idx):
            if buyi < selli and prices[selli]-prices[buyi] > profit:
                profit = prices[selli]-prices[buyi]
        
        return max(0, profit)
        