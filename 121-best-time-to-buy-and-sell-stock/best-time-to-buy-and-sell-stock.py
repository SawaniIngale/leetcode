class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # min_price = float('inf')
        # max_profit = 0

        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif max_profit < price - min_price:
        #         max_profit = price - min_price

        # return max_profit

        #Sliding window approach

        l = 0
        max_profit = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]

            if profit > 0:
                max_profit = max(profit, max_profit)

            else:
                l = r
        return max_profit