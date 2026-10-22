class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        l,r = 0, len(values)-1
        index = -1
        while l <= r:
            m = (l+r) // 2
            if values[m][1] == timestamp:
                index = m
                break
            elif values[m][1] < timestamp:
                l = m+1
            else:
                r = m-1
        if index == -1:
            return ""
        return values[index][0]
        
            

        
