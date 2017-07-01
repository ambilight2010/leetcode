class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        min_value = prices[0]
        for p in prices:
            min_value = min(p, min_value)
            max_profit = max(p - min_value, max_profit)
        return max_profit

