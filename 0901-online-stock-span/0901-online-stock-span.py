class StockSpanner:
    def __init__(self):
        self.stack = [(inf, 0)]

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

#     def __init__(self):
#         self.stock_prices = []
        

#     def next(self, price: int) -> int:
#         n = len(self.stock_prices)        
#         count = 1
#         while n > 0 and price >= self.stock_prices[n-1][0]:
#             count += self.stock_prices[n-1][1]
#             n -= self.stock_prices[n-1][1]
#         self.stock_prices.append((price, count))
#         return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)