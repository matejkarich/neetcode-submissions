class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def dfs(index, runningSum):

            if runningSum == amount:
                 return 0

            if runningSum > amount or index >= len(coins):
                return 10**18

            if (index,runningSum) in cache:
                return cache[(index,runningSum)]

            sameCoin = 10**18
            if coins[index] > 0:
                sameCoin = dfs(index, runningSum+coins[index]) + 1
            skipCoin = dfs(index+1, runningSum)

            cache[(index,runningSum)] = min(sameCoin, skipCoin)
            return cache[(index,runningSum)]

        result = dfs(0, 0)
        if result == 10**18:
            return -1
        return result
