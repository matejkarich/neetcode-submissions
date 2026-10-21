class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        maxArea = 0
        while start < end:
            currentArea = (end-start) * min(heights[start], heights[end])
            maxArea = max(maxArea, currentArea)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return maxArea
