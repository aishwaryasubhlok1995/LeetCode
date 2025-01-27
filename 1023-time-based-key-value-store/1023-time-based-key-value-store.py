class TimeMap:

    def __init__(self):
        self.dictTime = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictTime:
            self.dictTime[key] = [[timestamp, value]]  
        else:
             self.dictTime[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictTime:
            return ""
        sortedValues = self.dictTime[key]
        if sortedValues[0][0] > timestamp:
            return ""
        i = len(sortedValues) - 1
        while i>=0:
            if sortedValues[i][0] <= timestamp:
                return sortedValues[i][1]
            i -= 1

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)