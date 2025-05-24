class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        # trivial approach
        # tc: O(N2)
        # for buy_day in range(n):
        #     for sell_day in range(buy_day+1, n):
        #         if prices[buy_day] < prices[sell_day]:
        #             profit = prices[sell_day] - prices[buy_day]
        #             max_profit = max(max_profit, profit)
        # return max_profit

        cheapest_price = float('inf')
        max_profit = 0

        for cur_price in prices:
            if cur_price < cheapest_price:
                cheapest_price = cur_price
            else:
                profit = cur_price - cheapest_price
                max_profit = max(max_profit, profit)
        return max_profit