class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0

        while any(pos <= target for pos in position):
            is_fleet = False
            pos = position.pop()
            for index, p in enumerate(position):
                if p == pos:
                    position.pop(index)
                    is_fleet = True
            if is_fleet:
                fleets += 1
            else:
                position.append(pos)

            position = [position[i]+speed[i] for i in range(len(position))]
            print(position)

        return fleets + len(position)



