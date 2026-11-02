class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(index, runningSum, coinCount):

            if runningSum == amount:
                 return coinCount

            if runningSum > amount or index >= len(coins):
                return 10**18

            sameCoin = 10**18
            if coins[index] > 0:
                sameCoin = dfs(index, runningSum+coins[index], coinCount+1)
            skipCoin = dfs(index+1, runningSum, coinCount)

            return min(sameCoin, skipCoin)

        result = dfs(0, 0, 0)
        if result == 10**18:
            return -1
        return result
