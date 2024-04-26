class Node:
    def __init__(self, key, value):
        self.key= key
        self.val = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.LRU = Node(0, 0)
        self.MRU = Node(0, 0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
    
    def remove(Self, Node):
        prev  = Node.prev
        nextt = Node.next 
        prev.next = nextt
        nextt.prev = prev
    
    def insert(self, Node):
        prev = self.MRU.prev
        nextt = self.MRU
        prev.next = self.MRU.prev = Node
        Node.prev = prev 
        Node.next = self.MRU 
    
            
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
             self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert( self.cache[key])
        
        if len(self.cache) > self.cap:
            leastRu = self.LRU.next 
            self.remove(leastRu)
            del self.cache[leastRu.key]
        
            
       
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)