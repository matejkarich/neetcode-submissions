class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}

        def dfs(i, remAmount):

            if remAmount < 0:
                return 0

            if remAmount == 0:
                return 1

            if i == len(coins):
                return 0

            if (i, remAmount) in cache:
                return cache[(i, remAmount)]

            cache[(i, remAmount)] = dfs(i, remAmount-coins[i]) + dfs(i+1, remAmount)
            return cache[(i, remAmount)]

        return dfs(0, amount)
            
            

            