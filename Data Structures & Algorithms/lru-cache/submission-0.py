class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        nex = None
        while capacity > 0:
            node = ListNode(-1, None, nex)
            if nex:
                nex.prev = node
            nex = node
            capacity -= 1
        self.head = nex
        self.priority = nex
        while nex.next:
            nex = nex.next
        self.tail = nex
        self.cache = {}

    def get(self, key: int) -> int:
        val, node = self.cache.get(key, (-1, None))
        if node:
            if node.prev:
                node.prev.next = node.next
                node.prev = None
                node.next = self.head
                self.head = node
        return val

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            _, node = self.cache.get(key)
            node.val = value
            self.cache[key] = (value, node)
        else:
            node = self.tail 
            node.val = value
            if node.prev:
                node.prev.next = None
                self.tail = node.prev
                node.prev = None
                node.next = self.head
                self.head = node
            self.cache[key] = (value, node)
            
