class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {};
        self.pipe = []
        self.capacity = capacity
            
    def get(self, key: int) -> int:
        if key in self.cache:
            self.pipe.remove(key)
            self.pipe.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.pipe) == self.capacity and key not in self.pipe:
            elementToRemove = self.pipe.pop(0)
            del self.cache[elementToRemove]
        #if len(self.pipe) <= self.capacity or ((len(self.pipe) != 0 and self.pipe[len(self.pipe)-1] != key)): 
        if key in self.pipe:
            self.pipe.remove(key)
        self.pipe.append(key)
        self.cache[key] = value
            
       
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)