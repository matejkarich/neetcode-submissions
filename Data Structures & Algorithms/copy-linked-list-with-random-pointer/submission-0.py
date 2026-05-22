"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        hashMap = {}
        while current:
            hashMap[current] = Node(current.val, None, None)
            current = current.next

        current = head
        while current:
            copy = hashMap[current]
            copy.next = hashMap[current.next] if current.next in hashMap.keys() else None
            copy.random = hashMap[current.random] if current.random in hashMap.keys() else None
            current = current.next

        return hashMap[head]

        