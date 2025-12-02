class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = prices[0]
        profit = 0
        i = 1

        while i < len(prices):
            if prices[i] < buy :
                buy = prices[i]
            else :
                new_profit = prices[i] - buy
                profit = max(profit, new_profit)
            i += 1

        return profit
        