class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallest, largest = 1, max(piles)
        result = largest
        
        while smallest <= largest:
            k = (smallest + largest) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)

            if hours <= h:
                result = min(result, k)
                largest = k-1
            else:
                smallest = k+1

        return result