class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        if n < 2: 
            return 0
        
        prev_buy, prev_sell, prev_nothing = -prices[0], 0, 0
        
        for i in range(1, n):
            buy  = max(max(prev_sell, prev_nothing) - prices[i], prev_buy) 
            sell = max(prev_buy + prices[i], prev_sell)
            nothing = max(prev_sell, prev_buy, prev_nothing)
            prev_buy, prev_sell, prev_nothing = buy, sell, nothing
            
        return max(sell, nothing)