class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        for price in prices:
            profit=price-minBuy
            maxP=max(maxP, profit)
            minBuy=min(minBuy, price)

        return maxP