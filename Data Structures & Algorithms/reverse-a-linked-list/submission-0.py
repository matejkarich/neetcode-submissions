# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        curr = head
        nex = head.next

        curr.next = None
        while nex is not None:
            temp = nex.next
            nex.next = curr
            curr = nex
            nex = temp
        
        return curr
        