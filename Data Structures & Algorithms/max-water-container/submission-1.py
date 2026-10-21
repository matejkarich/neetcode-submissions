class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        p1, p2 = 0, len(heights)-1
        while p1 < p2:
            area = min(heights[p1], heights[p2]) * (p2 - p1)
            maxArea = max(area, maxArea)
            if heights[p1] <= heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return maxArea