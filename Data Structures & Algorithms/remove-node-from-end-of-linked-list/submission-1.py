# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        head = self.reverseList(head)

        if n == 1:
            head = head.next

        prev = curr = head
        while curr and n > 1:
            prev = curr
            curr = curr.next
            n = n - 1
        prev.next = curr.next

        return self.reverseList(head)

    def reverseList(self, head):
        curr = head
        nex = head.next

        while nex:
            temp = nex.next
            nex.next = curr
            curr = nex
            nex = temp
        head.next = None

        return curr
        
        