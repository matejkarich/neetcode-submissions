class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}
        
        def dfs(i, buying):

            if i >= len(prices):
                return 0
            
            if (i, buying) in cache:
                return cache[(i, buying)]

            if buying:
                buyCoin = dfs(i+1, False)-prices[i]
                dontBuy = dfs(i+1, True)
                cache[(i, buying)] = max(buyCoin, dontBuy)
                return max(buyCoin, dontBuy)
            else:
                sellCoin = dfs(i+2, True) + prices[i]
                holdCoin = dfs(i+1, False)
                cache[(i, buying)] = max(sellCoin, holdCoin)
                return max(sellCoin, holdCoin)

        return dfs(0, True)