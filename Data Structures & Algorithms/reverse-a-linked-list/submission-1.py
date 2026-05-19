# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head
        nex = head.next

        while nex:
            temp = nex.next
            nex.next = curr
            curr = nex
            nex = temp
        head.next = None

        return curr

        