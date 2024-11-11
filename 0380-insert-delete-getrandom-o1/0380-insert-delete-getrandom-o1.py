import random
class RandomizedSet:

    def __init__(self):
        self.hm = {}
        self.randomlist = []

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        self.randomlist.append(val)
        self.hm[val] = len(self.randomlist) - 1
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False 
        idx = self.hm[val]
        lastValue = self.randomlist[-1]
        self.hm[lastValue] = idx 
        self.randomlist[idx] = lastValue
        self.randomlist.pop() 
        del self.hm[val]
        return True 
        
    def getRandom(self) -> int:
        #return random.choice(self.randomlist)
        idx = random.randint(0, len(self.randomlist) - 1)
        return self.randomlist[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()