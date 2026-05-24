class ListNode:
    def __init__(self, key, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node:
            if node.prev:
                node.prev.next = node.next
                if self.tail == node:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev
                node.prev = None
                node.next = self.head
                self.head.prev = node
                self.head = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1: # key exists in cache
            node = self.cache.get(key)
            node.val = value
        else:             # must add key to cache    
            if len(self.cache) >= self.capacity:         # no space left in cache, must evict node
                del self.cache[self.tail.key]
                evictNode = self.tail
                if evictNode.prev:
                    evictNode.prev.next = None
                if evictNode.next:
                    evictNode.next.prev = evictNode.prev
                self.tail = evictNode.prev
                evictNode = None
            newNode = ListNode(key, value, None, self.head)
            if self.head:
                self.head.prev = newNode
            self.head = newNode
            self.cache[key] = newNode
            if not self.tail:
                self.tail = newNode
            
