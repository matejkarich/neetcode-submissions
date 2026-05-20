# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head.next is None or head.next.next is None:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        nex = slow.next

        while nex:
            temp = nex.next
            nex.next = slow
            slow = nex
            nex = temp
        mid.next = None

        start = head
        while start.next and slow.next:
            temp = start.next
            start.next = slow
            temp2 = slow.next
            slow.next = temp
            slow = temp2
            start = temp

        return



        

        
        