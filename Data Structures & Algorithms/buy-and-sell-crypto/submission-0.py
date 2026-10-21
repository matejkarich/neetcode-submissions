class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if len(prices) < 2:
            return 0
        i, j = 0, 1
        while i < len(prices):
            while j < len(prices) and prices[j] > prices[i]:
                maxProfit = max(maxProfit, prices[j]-prices[i])
                j += 1
            i = j
            j += 1
        return maxProfit
            
