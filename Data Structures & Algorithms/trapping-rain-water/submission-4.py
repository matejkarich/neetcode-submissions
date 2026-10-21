class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        start, end = 0, len(height)-1
        lMax, rMax = height[start], height[end]
        while start < end:
            if lMax < rMax:
                start += 1
                lMax = max(lMax, height[start])
                trapped += lMax - height[start]
            else:
                end -= 1
                rMax = max(rMax, height[end])
                trapped += rMax - height[end]
        return trapped