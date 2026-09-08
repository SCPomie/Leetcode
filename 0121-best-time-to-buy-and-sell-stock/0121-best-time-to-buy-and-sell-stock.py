class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        buy = prices[0]
        maxP = 0

        for price in prices:
            buy = min(buy, price)
            maxP = max((maxP, price - buy))
        return maxP