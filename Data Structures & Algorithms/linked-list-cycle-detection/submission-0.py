# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: 
        visited = {}
        visited[head] = 1
        while head:
            head = head.next
            if head in visited:
                return True
            visited[head] = 1
        return False
        