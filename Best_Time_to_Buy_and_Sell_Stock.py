"""121. Best Time to Buy and Sell Stock[Medium]
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one 
share of the stock), design an algorithm to find the maximum profit.


Thinking:
1. No need to know which one transaction is
2. Buy in lowest and sell in highest
3. Sell afte buy
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
           return 0
        res = 0
        min_price = prices[0]

        for price in prices:
           if price<min_price:
               min_price = price
           else:
               res = max(price-min_price, res)
        return res

"""122. Best Time to Buy and Sell Stock II [Medium]
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions 
as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, 
you must sell the stock before you buy again).

Thinking:
1. No need to know which one transaction is
2. Buy in lowest and sell in highest
3. Sell afte buy
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size==0:
           return 0
        res = 0
        for i in xrange(1, size):
            if prices[i]>prices[i-1]:
                res += prices[i]-prices[i-1]
        return res

"""122. Best Time to Buy and Sell Stock III [Hard]
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.

Thinking:
1. No need to know which one transaction is
2. Buy in lowest and sell in highest
3. Two transactions means combinations
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size==0:
            return 0

        min_val = prices[0]
        left_max_profit = 0
        left_profits = [0 for i in range(0, size+1)]
        
        for i in xrange(1, size):
            if prices[i]<min_val:
                min_val = prices[i]
            else:
                left_max_profit = prices[i]-min_val
            left_profits[i] = left_max_profit

        max_val = prices[-1]
        right_max_profit = 0
        res = left_profits[-1]

        for j in xrange(size-1, 0, -1):
            if prices[j]>max_val:
                max_val = prices[j]
            else:
                right_max_profit = max(right_max_profit, max_val-prices[j])
            res = max(res, right_max_profit+left_profits[j])

        return res

"""188. Best Time to Buy and Sell Stock IV [Hard]
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices):
        if size == 0:
            return 0

        if k>=size:
            self.solveMaxProfit(prices)

        global_max = [0 for i in range(0, k+1)]
        local_max  = [0 for i in range(0, k+1)]

        for j in xrange(1, size):
            diff = prices[i]-prices[i-1]
            for i in xrange(k, 0, -1):
                local_max[i] = max(global_max[i-1]+max(diff,0), local_max[i]+diff)
                global_max[i]  = max(local_max[i], global_max[i])

        return global_max[k]

    def solveMaxProfit(prices):
        res = 0 
        for i in xrange(1, len(prices)):
            if prices[i]>prices[i-1]:
                res += prices[i]-prices[i-1]
        return res

