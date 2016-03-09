"""
sells: The highest profit if the stock is not held at day i
buys: The highest profit if the stock is held at day i
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if days == 0 or days == 1:
            return 0
        buys = [None]*days
        sells = [None]*days
        sells[0] = 0
        sells[1] = max(0, prices[1]-prices[0])
        buys[0] = -prices[0]
        buys[1] = max(-prices[0],-prices[1])

        for x in xrange(2, days):
            sells[x] = max(sells[x-1], buys[x-1]+prices[x])
            buys[x]  = max(buys[x-1], sells[x-2]-prices[x])

        return sells[-1]