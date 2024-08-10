class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([value, timestamp])
        else:
            self.timeMap[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        values = self.timeMap[key]
        i = 0
        j = len(values)-1
        if timestamp < values[0][1]:
            return ""
        while i < j:
            middle = (i+j)//2
            if values[middle][1] == timestamp:
                return values[middle][0]
            elif values[middle][1]<=timestamp:
                i = middle +1
            else:
                j = middle
            if timestamp < values[i][1]:
                return values[i-1][0]
        return values[i][0] 
               

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)