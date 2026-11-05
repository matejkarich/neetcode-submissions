class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}
        
        def dfs(i, buyPrice):

            if i >= len(prices):
                return 0
            
            if (i, buyPrice) in cache:
                return cache[(i, buyPrice)]

            if buyPrice < 0:
                buyCoin = dfs(i+1, prices[i])
                dontBuy = dfs(i+1, -1)
                cache[(i, buyPrice)] = max(buyCoin, dontBuy)
                return max(buyCoin, dontBuy)
            else:
                sellCoin = dfs(i+2, -1) + prices[i]-buyPrice
                holdCoin = dfs(i+1, buyPrice)
                cache[(i, buyPrice)] = max(sellCoin, holdCoin)
                return max(sellCoin, holdCoin)

        return dfs(0, -1)