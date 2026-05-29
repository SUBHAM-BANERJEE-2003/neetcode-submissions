class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        lowestsofar = prices[0]
        for price in prices:
            maxprof = max(maxprof, price - lowestsofar)
            lowestsofar = min(lowestsofar, price)
        return maxprof
            
