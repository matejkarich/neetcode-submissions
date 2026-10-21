class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = [(p,s) for p,s in zip(position, speed)]
        positions = sorted(positions)

        stack = []
        for i in range(len(positions)-1, -1, -1):
            arrival_time = (target - positions[i][0]) / positions[i][1]
            stack.append(arrival_time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

